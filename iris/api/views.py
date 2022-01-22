from rest_framework import viewsets

from iris.api.serializers import IrisSerializer
from iris.models import Iris


class IrisViewSet(viewsets.ModelViewSet):
    queryset = Iris.objects.all()
    serializer_class = IrisSerializer
    lookup_field = "id"
