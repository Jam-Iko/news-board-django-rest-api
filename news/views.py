from news.models import Post, Comment
from news.serializers import PostSerializer
from news.serializers import CommentSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "posts": reverse("post-list", request=request, format=format),
            "comments": reverse("comment-list", request=request, format=format),
        }
    )


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvoteView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.upvotes += 1
        post.save()
        return Response(
            {"post_id": post.id, "post_title": post.title, "post_upvotes": post.upvotes}
        )
