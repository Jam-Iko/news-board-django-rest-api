# Generated by Django 3.1 on 2020-08-18 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(name="post", options={"ordering": ["-created"]},),
        migrations.AlterField(
            model_name="comment",
            name="content",
            field=models.TextField(blank=True, default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="post",
            name="upvotes",
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
