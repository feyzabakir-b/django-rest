from django.urls import path
from news.api import views as api_views


urlpatterns = [
    path('articles/', api_views.ArticleListCreateAPIView.as_view(), name='article_list'),
    path('articles/<int:pk>', api_views.ArticleDetailAPIView.as_view(), name='article-detail')
]


## Function base view ##

# urlpatterns = [
#     path('articles/', api_views.article_list_create_view, name='article_list'),
#     path('articles/<int:pk>', api_views.article_detail_api_view, name='article-detail')
# ]
