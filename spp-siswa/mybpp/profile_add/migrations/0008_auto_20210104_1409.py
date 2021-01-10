# Generated by Django 3.1.5 on 2021-01-04 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_add', '0007_tingkat_siswa_kelas_x'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tingkat_siswa',
            old_name='Kelas_x',
            new_name='x',
        ),
        migrations.AddField(
            model_name='tingkat_siswa',
            name='xi',
            field=models.CharField(choices=[('X', 'X'), ('XI', 'XI'), ('XII', 'XII')], default='XI', max_length=255),
        ),
        migrations.AddField(
            model_name='tingkat_siswa',
            name='xii',
            field=models.CharField(choices=[('X', 'X'), ('XI', 'XI'), ('XII', 'XII')], default='XII', max_length=255),
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_siswa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profile_add.identitas')),
            ],
        ),
    ]
