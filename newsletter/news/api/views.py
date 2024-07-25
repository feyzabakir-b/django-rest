from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from news.models import Article
from news.api.serializers import ArticleSerializer

#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class ArticleListCreateAPIView(APIView):
    def get(self, request):
        articles = Article.objects.filter(activate=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data) 
    
    def post(self, request): 
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):
    def get_object(self, pk):
        article_instance = get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        article_instance = self.get_object(pk=pk)
        serializer = ArticleSerializer(article_instance)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article_instance = self.get_object(pk=pk)
        serializer = ArticleSerializer(article_instance, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk):
        article_instance = self.get_object(pk=pk) 
        article_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ## Function Method ##
# @api_view(['GET', 'POST'])
# def article_list_create_view(request):
    
#     if request.method == 'GET':
#         articles = Article.objects.filter(activate=True)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     elif request.method=='POST':
#        serializer = ArticleSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(status=status.HTTP_400_BAD_REQUEST) 
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail_api_view(request, pk):
#     try:
#         article_instance = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#        return Response(
#            {
#                'errors':{
#                    'code': 404,
#                    'message': f'No article was found with such an id {{pk}}.'
#                }
#            },
#            status=status.HTTP_400_BAD_REQUEST
#        )
    
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article_instance)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#        serializer = ArticleSerializer(article_instance, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(status=status.HTTP_400_BAD_REQUEST) 
    
#     elif request.method == 'DELETE':
#         article_instance.delete()
#         return Response(
#             {
#                'errors':{
#                    'code': 404,
#                    'message': f'The article with ID number {{pk}} has been deleted.'
#                }
#            },
#            status=status.HTTP_204_NO_CONTENT
#         )
