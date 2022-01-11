from django.contrib import admin

# Register your models here.
from common.models import APIsGroup, APIsObject, APIsMethod, APIsAccessControl


@admin.register(APIsGroup)
class APIsGroupAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    filter_horizontal = ["user", ]
    list_filter = ("group_name",)
    list_display = (
        "id",
        "group_name",
        "group_describe",
    )


@admin.register(APIsObject)
class APIsObjectAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_filter = ("viewsets_name", "display_name",)
    list_display = (
        "id",
        "viewsets_name",
        "display_name",
    )


@admin.register(APIsMethod)
class APIsMethodAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_filter = ("apis_group",
                   "list_method",
                   "retrieve_method",
                   "create_method",
                   "update_method",
                   "partial_update_method",
                   "destroy_method",
                   "apis_object",)
    list_editable = [
        "list_method",
        "retrieve_method",
        "create_method",
        "update_method",
        "partial_update_method",
        "destroy_method",
    ]
    list_display = (
        "apis_group",
        "apis_object",
        "list_method",
        "retrieve_method",
        "create_method",
        "update_method",
        "partial_update_method",
        "destroy_method",

    )


@admin.register(APIsAccessControl)
class APIsAccessControlAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"

    list_filter = ("user",
                   "apisgroup",
                   )
    list_display = (
        "id",
        "user",
        "apisgroup",
    )
