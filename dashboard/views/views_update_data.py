from ..models import Siswa
from django.shortcuts import render,redirect,get_object_or_404
from ..services import update_services
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_POST


@login_required
@require_POST
def UpdateSiswa(request,id):
  if request.method == 'POST':
    data = {
      'id':id,
      'nama_lengkap': request.POST.get('nama_lengkap'),
      'nik': request.POST.get('nik') or None,
      'nis': request.POST.get('nis') or None,
      'nisn': request.POST.get('nisn') or None,
      'tahun_lahir': request.POST.get('tahun_lahir'),
      'alamat_lengkap': request.POST.get('alamat_lengkap'),
      'kontak': request.POST.get('kontak'),
      }
    result =  update_services(**data)
    
    if result.get('status'):
      messages.success(request,f'{result.get('messages')}')
      return redirect('dashboard_app:list_data')
    else:
      messages.error(request,f'{result.get('messages')}')
      return redirect('dashboard_app:list_data')
  return redirect('dashboard_app:list_data')

@login_required
@require_POST
def delete_siswa(request, id):
    siswa_obj = get_object_or_404(Siswa, id=id)
    siswa_obj.delete()
    return redirect('dashboard_app:list_data')

