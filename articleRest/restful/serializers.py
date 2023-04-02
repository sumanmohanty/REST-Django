from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    article = serializers.CharField(max_length=1000, required=True)

    def create(self, validated_data):
        return Article.objects.create(
            article=validated_data.get('article')
        )

    def update(self, instance, validated_data):
        instance.article = validated_data.get('article', instance.text)
        instance.save()
        return instance

    class Meta:
        model = Article
        fields = (
            'articleID',
            'article'
        )
