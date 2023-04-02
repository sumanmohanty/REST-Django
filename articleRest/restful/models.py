from django.db import models

# Create your models here.


class Article(models.Model):
    articleID = models.AutoField(
        primary_key=True
    )

    article = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False
    )

    last_updated = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'articles'
