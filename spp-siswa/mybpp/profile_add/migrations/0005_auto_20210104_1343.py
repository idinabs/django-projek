# Generated by Django 3.1.5 on 2021-01-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_add', '0004_auto_20210104_1342'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Kelas_Siswa',
        ),
        migrations.AddField(
            model_name='identitas',
            name='TKJ',
            field=models.CharField(choices=[('TKJ', 'Teknik Komputer & Jaringan'), ('Multimedia', 'Multimedia'), ('Akuntansi', 'Akuntansi'), ('Tata Busana', 'Tata Busana'), ('Perbankan Syariah', 'Perbankan Syariah'), ('Tata Boga', 'Tata Boga'), ('TKKR', 'TKKR'), ('OTKP', 'OTKP'), ('BDP', 'BDP'), ('DKV', 'DKV'), ('Animasi', 'Animasi')], default='TKJ', max_length=255),
        ),
    ]
