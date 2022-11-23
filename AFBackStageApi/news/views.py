from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import News
from .serializers import NewsListModelSeralizers, NewsDetailModelSeralizers


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10  # 指定每页显示多少条数据
    page_query_param = 'page'  # URL中页码的参数
    page_size_query_param = 'size'  # URL参数中每页显示条数的参数
    max_page_size = 30  # 每页最多显示多少条数据


class NewsListViewSet(ListModelMixin,RetrieveModelMixin, GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsListModelSeralizers
    pagination_class = LargeResultsSetPagination


class NewsDetailViewSet(ListModelMixin,RetrieveModelMixin, GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsDetailModelSeralizers
    pagination_class = LargeResultsSetPagination
