from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from news import views

urlpatterns = format_suffix_patterns(
    [
        path("", views.api_root),
        path("posts/", views.PostListView.as_view(), name="post-list"),
        path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
        path("comments/", views.CommentListView.as_view(), name="comment-list"),
        path(
            "comments/<int:pk>/",
            views.CommentDetailView.as_view(),
            name="comment-detail",
        ),
        path("posts/<int:pk>/upvote/", views.UpvoteView.as_view(), name="upvote-view"),
    ]
)
