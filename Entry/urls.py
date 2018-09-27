from django.urls import path, include
from . import views

from django.views.generic.base import TemplateView
app_name = 'Entry'

urlpatterns = [
    path('', views.index,  name = 'index'),
    path('categories/', views.categories, name = 'categories'),
    path('categories/<int:category_id>', views.category, name = 'category'),
    path('categories/new', views.new_category, name = 'new_category'),
    path('posts/', views.posts, name = 'posts'),
    path('posts/<int:post_id>', views.post, name = 'post'),
    path('posts/new', views.new_post, name = 'new_post'),
    path('users/', views.users, name = 'users'),
    path('users/<str:username>', views.user , name = 'user'),
    # path('posts/newcomment', views.new_comment, name='new_comment'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]