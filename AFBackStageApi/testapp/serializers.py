from rest_framework import serializers




# 创建序列化器类
from testapp.models import User


class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
