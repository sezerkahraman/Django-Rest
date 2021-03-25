from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, DestroyAPIView, RetrieveUpdateAPIView, \
    CreateAPIView

from post.api.permissions import IsOwner #Custom permission import edildi.
from post.api.serializers import PostSerializer, CreateSerializer
from post.models import Post
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class PostListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]
    def perform_update(self,serializer):
        serializer.save(user=self.request.user)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreateSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

