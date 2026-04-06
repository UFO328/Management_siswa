from ..models import Siswa
from django.db import IntegrityError

def update_services(**kwargs):
    try:
      siswa = Siswa.objects.get(id=kwargs.get('id'))
      siswa.nama_lengkap = kwargs.get('nama_lengkap')
      siswa.nik = kwargs.get('nik')
      siswa.nis = kwargs.get('nis') or None
      siswa.nisn = kwargs.get('nisn') or None
      siswa.tahun_lahir = kwargs.get('tahun_lahir')
      siswa.alamat_lengkap = kwargs.get('alamat_lengkap')
      siswa.kontak = kwargs.get('kontak')
      siswa.save()
      return {'status':True,'messages':'DATA BERHASIL DI UPDATE'}
    except Siswa.DoesNotExist:
      return {'status':False,'messages':'DATA TIDAK DI TEMUKAN'}
