from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from news.models import Article
from news.api.serializers import ArticleSerializer

@api_view(['GET'])
def article_list_create_view(request):
    
    if request.method == 'GET':
        articles = Article.objects.filter(activate=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    