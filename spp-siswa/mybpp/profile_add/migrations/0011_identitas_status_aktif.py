# Generated by Django 3.1.5 on 2021-01-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_add', '0010_auto_20210104_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='identitas',
            name='status_aktif',
            field=models.CharField(choices=[('Aktif', 'Aktif')], default='Aktif', max_length=50),
        ),
    ]
