from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = []

router = DefaultRouter()

router.register('list',views.SolutionListViewSet)
router.register('detail',views.SolutionDetailViewSet)

urlpatterns+=router.urls