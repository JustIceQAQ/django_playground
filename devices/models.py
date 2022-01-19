from django.db import models

# Create your models here.
from django.utils import timezone


class Devices(models.Model):
    name = models.CharField("裝置名稱", max_length=20)


class Properties(models.Model):
    label = models.CharField("資料名稱", blank=True, null=True, max_length=20)
    value = models.CharField("資料數值", blank=True, null=True, max_length=20)
    create_at = models.DateTimeField("資料建立時間", default=timezone.now, db_index=True)
    device = models.ForeignKey(Devices, verbose_name="相依裝置", on_delete=models.CASCADE, )
