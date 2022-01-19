from django.db import models
from django.utils.translation import gettext_lazy as _
import architect

# Create your models here.
class Device(models.Model):
    name = models.CharField(_("裝置名稱"), max_length=15)
# @architect.uninstall('partition')
@architect.install('partition', type='range', subtype='date', constraint='month', column='create_at')
class Historical(models.Model):
    name = models.CharField(_("資料名稱"), max_length=15, blank=True, null=True)
    value = models.TextField(_("資料數值"), blank=True, null=True)
    create_at = models.DateTimeField(_("新增日期"))
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
