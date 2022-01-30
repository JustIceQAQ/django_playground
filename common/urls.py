from django.urls import path

from common.views import swagger_index, markdown_index

common_urlpatterns = [
    path("swagger_index/", swagger_index, name="swagger_index"),
    path("markdown_index/", markdown_index, name="markdown_index")
]