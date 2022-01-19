# Generated by Django 3.2.6 on 2022-01-18 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='裝置名稱')),
            ],
        ),
        migrations.CreateModel(
            name='Historical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True, verbose_name='資料名稱')),
                ('value', models.TextField(blank=True, null=True, verbose_name='資料數值')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='新增日期')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
        ),
    ]