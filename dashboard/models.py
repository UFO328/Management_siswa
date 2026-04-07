from django.db import models

class Siswa(models.Model):
    nama_siswa = models.CharField(max_length=225)
    nik = models.CharField(max_length=225, unique=True)
    nis = models.CharField(max_length=225, unique=True)
    nisn = models.CharField(max_length=225, unique=True)
    tahun_lahir = models.CharField(max_length=25)
    alamat_lengkap = models.TextField()
    kontak = models.CharField(max_length=225)

    def __str__(self):
        return self.nama_siswa


class DaftarMapel(models.Model):
    mapel = models.CharField(max_length=225)

    def __str__(self):
        return self.mapel


class DaftarKelas(models.Model):
    kelas = models.CharField(max_length=225)

    def __str__(self):
        return self.kelas


class SiswaKelas(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    kelas = models.ForeignKey(DaftarKelas, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('siswa', 'kelas')  # mencegah double input

    def __str__(self):
        return f"{self.siswa} - {self.kelas}"


class NilaiSiswa(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    mapel = models.ForeignKey(DaftarMapel, on_delete=models.CASCADE)
    nilai = models.IntegerField()

    class Meta:
        unique_together = ('siswa', 'mapel')  # satu siswa satu nilai per mapel

    def __str__(self):
        return f"{self.siswa} - {self.mapel} ({self.nilai})"