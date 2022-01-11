from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from iris.models import Iris
from iris.serializers import IrisSerializer


class IrisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Iris.objects.all()
    serializer_class = IrisSerializer
    permission_classes = [permissions.IsAuthenticated]
