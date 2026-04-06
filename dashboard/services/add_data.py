from ..models import Siswa
from django.db import IntegrityError

def add_data_services(**kwargs):
    nama_lengkap = kwargs.get('nama_lengkap')

    # Validasi data sudah ada
    if Siswa.objects.filter(nama_lengkap=nama_lengkap).exists():
        return {'status': False, 'messages': 'DATA SUDAH TERSEDIA'}

    try:
        Siswa.objects.create(**kwargs)
        return {'status': True, 'messages': 'BERHASIL MENAMBAHKAN DATA'}
    
    except IntegrityError:
        return {'status': False, 'messages': 'GAGAL MENAMBAHKAN DATA (DUPLIKASI)'}