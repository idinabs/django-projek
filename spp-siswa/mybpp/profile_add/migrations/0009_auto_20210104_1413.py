# Generated by Django 3.1.5 on 2021-01-04 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_add', '0008_auto_20210104_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='siswa',
            name='kelas_siswa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profile_add.kelas_siswa'),
        ),
        migrations.AddField(
            model_name='siswa',
            name='tingkat_siswa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profile_add.tingkat_siswa'),
        ),
    ]
