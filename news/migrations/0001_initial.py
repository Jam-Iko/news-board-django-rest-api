# Generated by Django 3.1 on 2020-08-17 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(blank=True, default="", max_length=64)),
                ("title", models.CharField(blank=True, default="", max_length=255)),
                ("link", models.URLField(max_length=255)),
                ("upvotes", models.IntegerField(default=0)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("author", models.CharField(blank=True, default="", max_length=64)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="news.post",
                    ),
                ),
            ],
            options={"ordering": ["-created"],},
        ),
    ]