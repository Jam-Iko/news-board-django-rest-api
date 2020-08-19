from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, default="")
    link = models.URLField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64, blank=True, default="")
    upvotes = models.IntegerField(editable=False, default=0)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.title} by {self.author} read more at {self.link}"


class Comment(models.Model):
    content = models.TextField(max_length=255, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64, blank=True, default="")
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.author}: {self.content}"
