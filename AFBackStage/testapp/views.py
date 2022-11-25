# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from testapp.models import User
from testapp.serializers import TestModelSerializer

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10  # 指定每页显示多少条数据
    page_query_param = 'page'  # URL中页码的参数
    page_size_query_param = 'size'  # URL参数中每页显示条数的参数
    max_page_size = 30  # 每页最多显示多少条数据


class TestViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = TestModelSerializer
    pagination_class = LargeResultsSetPagination