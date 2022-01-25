"""django_playground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken.views import obtain_auth_token

from iris.views import IrisListView, IrisCreateView, IrisUpdateView, IrisDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

]

urlpatterns += [
    path('iris/', IrisListView.as_view(template_name="index.html")),
    path('iris/create/', IrisCreateView.as_view(template_name="iris/iris_create_form.html"), name='iris-create'),
    path('iris/update/<int:pk>/', IrisUpdateView.as_view(template_name="iris/iris_update_form.html"),
         name='iris-update'),
    path('iris/delete/<int:pk>/', IrisDeleteView.as_view(template_name="iris/iris_delete_form.html"),
         name='iris-delete'),
]

urlpatterns += [
    path('api/', include('iris.urls', namespace='iris')),
    path(r'api/token-auth/', obtain_auth_token)

]

urlpatterns += [
    path(r'api/api-token/', include('knox.urls'))
]
