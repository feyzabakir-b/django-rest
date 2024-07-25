from django.urls import path
from news.api import views as api_views

urlpatterns = [
    path('articles/', api_views.article_list_create_view, name='article_list'),
]
