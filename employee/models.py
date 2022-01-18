from django.db import models
from django.utils.translation import gettext_lazy as _
from psqlextra.types import PostgresPartitioningMethod
from psqlextra.models import PostgresPartitionedModel


# Create your models here.

class Employee(models.Model):
    name = models.CharField(_("姓名"), max_length=100)

    class SexChoices(models.IntegerChoices):
        Female = 0, _('Female')
        Male = 1, _('Male')
        __empty__ = _('(Unknown)')

    email = models.EmailField(blank=True, null=True)
    sex = models.IntegerField(choices=SexChoices.choices, blank=True, null=True)
    birthday = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Employee - [員工]")
        verbose_name_plural = _("Employee - [員工]")


class EmployeePartitione(PostgresPartitionedModel):
    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ["birthday"]

    name = models.CharField(_("姓名"), max_length=100)

    class SexChoices(models.IntegerChoices):
        Female = 0, _('Female')
        Male = 1, _('Male')
        __empty__ = _('(Unknown)')

    email = models.EmailField(blank=True, null=True)
    sex = models.IntegerField(choices=SexChoices.choices, blank=True, null=True)
    birthday = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("EmployeePartitione - [員工Partitione]")
        verbose_name_plural = _("EmployeePartitione - [員工Partitione]")
