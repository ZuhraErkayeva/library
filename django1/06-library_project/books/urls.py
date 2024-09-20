from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.home_view),
    path('authors/', views.author_view),
    path('categories/', views.category_view),
]