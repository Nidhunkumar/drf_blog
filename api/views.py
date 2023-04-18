from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User




from .permission import IsOwnerOrReadOnly
from .serializers import UserSerializer,PostSerializer,CommentSerializer,CategorySerializer
from .models import Post,Comment,Category

class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class PostList(generics.ListCreateAPIView):

    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ]

    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    
class CommentList(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class CategoryList(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
