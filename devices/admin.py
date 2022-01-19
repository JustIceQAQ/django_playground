from django.contrib import admin

from devices.models import Device, Historical


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Historical)
class HistoricalAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "value",
        "create_at",
        "device",
    )
