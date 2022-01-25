from django.urls import path
from rest_framework import routers

from iris.api.views import IrisViewSet
from iris.views import IrisListView, IrisCreateView, IrisUpdateView, IrisDeleteView

router = routers.DefaultRouter()
app_name = "iris"
router.register(r'iris', IrisViewSet, basename="iris")
urlpatterns = router.urls

iris_urlpatterns_view = [
    path('iris/', IrisListView.as_view(template_name="index.html")),
    path('iris/create/', IrisCreateView.as_view(template_name="iris/iris_create_form.html"), name='iris-create'),
    path('iris/update/<int:pk>/', IrisUpdateView.as_view(template_name="iris/iris_update_form.html"),
         name='iris-update'),
    path('iris/delete/<int:pk>/', IrisDeleteView.as_view(template_name="iris/iris_delete_form.html"),
         name='iris-delete'),
]