from django.db import models

class Siswa(models.Model):
    nama_lengkap = models.CharField(max_length=255, unique=True)
    nik = models.CharField(max_length=35, unique=True)
    nis = models.CharField(max_length=35, unique=True)
    nisn = models.CharField(max_length=35, unique=True)
    tahun_lahir = models.CharField(max_length=20)
    alamat_lengkap = models.CharField(max_length=255)
    kontak = models.CharField(max_length=255)  # Hapus unique=True