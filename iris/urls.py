from rest_framework import routers

from iris.api.views import IrisViewSet

router = routers.DefaultRouter()
app_name = "iris"
router.register(r'iris', IrisViewSet, basename="iris")
urlpatterns = router.urls
