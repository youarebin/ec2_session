from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, **kwargs): # Override
        id = self.kwargs['post_id']
        return self.queryset.filter(post=id)