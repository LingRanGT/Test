from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from solution.models import SolutionModel

from solution.serializers import SolutionListSerializer, SolutionDetailSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10  # 指定每页显示多少条数据
    page_query_param = 'page'  # URL中页码的参数
    page_size_query_param = 'size'  # URL参数中每页显示条数的参数
    max_page_size = 30  # 每页最多显示多少条数据


class SolutionListViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = SolutionModel.objects.all()
    serializer_class = SolutionListSerializer
    pagination_class = LargeResultsSetPagination


class SolutionDetailViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = SolutionModel.objects.all()
    serializer_class = SolutionDetailSerializer
    pagination_class = LargeResultsSetPagination
