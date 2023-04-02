from django.urls import path

from . import views

urlpatterns = [
    path('article/', views.ArticleView.as_view()),
    path('article/<int:articleID>/', views.ArticleView.as_view()),
]
