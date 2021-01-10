from django.db import models

class Identitas(models.Model):
    nama = models.CharField(max_length=255)
    pilihan_kelas = [
        ('Teknik Komputer & Jaringan', 'Teknik Komputer & Jaringan'),
        ('Multimedia', 'Multimedia'),
        ('Akuntansi', 'Akuntansi'),
        ('Tata Busana', 'Tata Busana'),
        ('Perbankan Syariah', 'Perbankan Syariah'),
        ('Tata Boga', 'Tata Boga'),
        ('TKKR', 'TKKR'),
        ('OTKP', 'OTKP'),
        ('BDP', 'BDP'),
        ('DKV', 'DKV'),
        ('Animasi', 'Animasi'),
    ]
    kelas = models.CharField(max_length=255, choices=pilihan_kelas, default='Teknik Komputer & Jaringan')

    tingkat = [
        ('X','X'),
        ('XI','XI'),
        ('XII','XII'),
    ]
    tingkat_kelas = models.CharField(max_length=255, choices=tingkat, default='X')



    aktif = [
        ('aktif','aktif')
    ]

    status_siswa = models.CharField(max_length=50, choices=aktif, default='aktif')

    def __str__(self):
        return self.nama


