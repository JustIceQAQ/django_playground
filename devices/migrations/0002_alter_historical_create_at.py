# Generated by Django 3.2.6 on 2022-01-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historical',
            name='create_at',
            field=models.DateTimeField(verbose_name='新增日期'),
        ),
    ]
