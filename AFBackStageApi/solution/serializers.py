from rest_framework import serializers

# 创建序列化器类
from solution.models import SolutionModel


class SolutionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionModel
        fields = ['id','picture', 'title', 'source', 'updated_time']


class SolutionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionModel
        fields = ['id','title', 'content']
