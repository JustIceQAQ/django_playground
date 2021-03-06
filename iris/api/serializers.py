from rest_framework import serializers

from iris.models import Iris


class IrisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iris
        fields = [
            "id",
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
            "classification",
        ]
