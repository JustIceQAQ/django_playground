from django.contrib import admin

from django.apps import apps

from devices.models import Devices, Properties


@admin.register(Devices)
class DevicesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name"
    ]


@admin.register(Properties)
class DevicesAdmin(admin.ModelAdmin):
    list_display = [
        "label",
        "value",
        "create_at",
        "device",
    ]
