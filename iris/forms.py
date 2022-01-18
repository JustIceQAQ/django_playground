from django import forms

from iris.models import Iris


class IrisModelForm(forms.ModelForm):
    class Meta:
        model = Iris
        fields = (
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
            "classification",
        )

