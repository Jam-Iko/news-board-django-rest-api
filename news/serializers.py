from rest_framework import serializers
from news.models import Post, Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        comment_data = validated_data.pop("comments")
        post = Post.objects.create(**validated_data)
        for comment in comment_data:
            Comment.objects.create(post=post, **comment_data)
        return post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "content", "created", "post"]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentCreateSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = "__all__"
