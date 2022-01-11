from rest_framework.permissions import BasePermission

from common.models import APIsMethod


class APIsMethodPermissionsModeSet:
    tolerant = any
    strict = all
    any = any
    all = all


class APIsMethodPermissions(BasePermission):

    def has_permission(self, request, view):
        runtime_user_api_group = request.user.user_api_group.all()

        runtime_view = view

        queryset = APIsMethod.objects.filter(apis_group__in=runtime_user_api_group,
                                             apis_object__viewsets_name=runtime_view.basename)

        is_it_all_allowed = []

        if queryset.exists():
            for item in queryset:
                if hasattr(item, f"{runtime_view.action}_method"):
                    is_it_all_allowed.append(getattr(item, f"{runtime_view.action}_method"))
                elif runtime_view.action is None:
                    # if runtime_view.action is None ... maybe is runtime_view.action value is OPTIONS
                    is_it_all_allowed.append(True)
        else:
            is_it_all_allowed.append(True)

        return (runtime_view.permission_api_method_mode(is_it_all_allowed)
                if hasattr(runtime_view, "permission_api_method_mode")
                else any(is_it_all_allowed))
