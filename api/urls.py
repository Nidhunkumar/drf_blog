from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api-auth/',include('rest_framework.urls')),
    path('', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)