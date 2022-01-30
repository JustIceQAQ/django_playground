from django.urls import path

from common.views import swagger_index

common_urlpatterns = [
    path("swagger_index/", swagger_index, name="swagger_index")
]