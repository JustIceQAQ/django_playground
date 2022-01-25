from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from iris.api.serializers import IrisSerializer
from iris.models import Iris


class IrisViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Iris.objects.all()
    serializer_class = IrisSerializer
    lookup_field = "id"
