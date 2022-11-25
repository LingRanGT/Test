from rest_framework import serializers
from .models import News


class NewsListModelSeralizers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'keyword', 'created_time']


class NewsDetailModelSeralizers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'keyword', 'source', 'created_time', 'content']
