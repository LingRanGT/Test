from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = []

router = DefaultRouter()
router.register('list', views.NewsListViewSet)
router.register('detail', views.NewsDetailViewSet)

urlpatterns+=router.urls