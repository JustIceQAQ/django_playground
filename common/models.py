from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class APIsGroup(models.Model):
    group_name = models.CharField(_("API群組名稱"), max_length=65535, unique=True)
    group_describe = models.TextField(_("API群組說明"), default=None,
                                      null=True,
                                      blank=True, )
    user = models.ManyToManyField(
        User,
        default=None,
        null=True,
        blank=True,
        verbose_name=_("相依 User"),
        through='APIsAccessControl',
        related_name="user_api_group",
        through_fields=('apisgroup', 'user'),

    )

    class Meta:
        verbose_name = _("APIGroup - [APIs 群組]")
        verbose_name_plural = _("APIGroup - [APIs 群組]")

    def __str__(self):
        return str(self.group_name)


class APIsAccessControl(models.Model):
    user = models.ForeignKey(User, default=None,
                             null=True,
                             blank=True, on_delete=models.SET_NULL,
                             verbose_name=_("相依 User"),
                             )
    apisgroup = models.ForeignKey(APIsGroup, default=None,
                                  null=True,
                                  blank=True, on_delete=models.SET_NULL,
                                  verbose_name=_("相依 APIsGroup"),
                                  )

    def __str__(self):
        return str(f"{self.user.username}:{self.apisgroup.group_name}")

    class Meta:
        verbose_name = _("APIsAccessControl - [APIs 存取控制]")
        verbose_name_plural = _("APIsAccessControl - [APIs 存取控制]")


class APIsObject(models.Model):
    viewsets_name = models.CharField(_("API Viewsets Name"), max_length=65535, unique=True)
    display_name = models.CharField(_("API Display Name"), max_length=65535)

    def __str__(self):
        return str(self.display_name)

    class Meta:
        verbose_name = _("APIsObject - [API 物件]")
        verbose_name_plural = _("APIsObject - [API 物件]")


def ox_format(value: bool) -> str:
    return "o" if value else "x"


class APIsMethod(models.Model):
    apis_group = models.ForeignKey(
        APIsGroup,
        verbose_name=_("相依 APIsGroup"),
        related_name="apimethod_apis_group",
        on_delete=models.CASCADE,
    )
    list_method = models.BooleanField(_("list 方法"))
    retrieve_method = models.BooleanField(_("retrieve 方法"))
    create_method = models.BooleanField(_("create 方法"))
    update_method = models.BooleanField(_("update 方法"))
    partial_update_method = models.BooleanField(_("partial_update 方法"))
    destroy_method = models.BooleanField(_("destroy 方法"))
    apis_object = models.ForeignKey(
        APIsObject,
        verbose_name=_("相依 APIsObject"),
        related_name="apimethod_apis_object",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return (f"{self.apis_object}: "
                f"{ox_format(self.list_method)}-"
                f"{ox_format(self.retrieve_method)}-"
                f"{ox_format(self.create_method)}-"
                f"{ox_format(self.update_method)}-"
                f"{ox_format(self.partial_update_method)}-"
                f"{ox_format(self.destroy_method)}")

    class Meta:
        verbose_name = _("APIsMethod - [API 功能]")
        verbose_name_plural = _("APIsMethod - [API 功能]")
