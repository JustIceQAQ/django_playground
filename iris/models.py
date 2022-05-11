from functools import partial
from django.db import models
from django.utils.translation import gettext_lazy as _

Decimal4_2 = partial(
    models.DecimalField,
    verbose_name="",
    max_digits=4,
    decimal_places=2
)

class Iris(models.Model):
    sepal_length = Decimal4_2(verbose_name=_("花萼長度"))
    sepal_width = Decimal4_2(verbose_name=_("花萼寬度"))
    petal_length = Decimal4_2(verbose_name=_("花瓣長度"))
    petal_width = Decimal4_2(verbose_name=_("花瓣寬度"))
    slices = models.PositiveIntegerField(verbose_name=_("花瓣片數"), default=0)

    class IrisClassification(models.TextChoices):
        SETOSA = 'setosa', _('山鳶尾')
        VERSICOLOR = 'versicolor', _('變色鳶尾')
        VIRGINICA = 'virginica', _('維吉尼亞鳶尾')

    classification = models.CharField(
        verbose_name="分類",
        max_length=15,
        choices=IrisClassification.choices,
        default=IrisClassification.SETOSA,
    )

    class Meta:
        verbose_name = _("Iris - [鳶尾花]")
        verbose_name_plural = _("Iris - [鳶尾花]")
