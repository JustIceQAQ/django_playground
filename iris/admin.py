from django.contrib import admin

# Register your models here.
from iris.models import Iris


@admin.register(Iris)
class IrisAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_filter = ["classification", ]
    list_display = [
        "id",
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "classification",
    ]
