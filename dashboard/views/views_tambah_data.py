from ..services import add_data_services
from django.shortcuts import render,redirect
from django.views import View 
from django.contrib import messages 
from django.contrib.auth.mixins import LoginRequiredMixin

class ViewAddData(LoginRequiredMixin,View):
  def get(self,request):
    return render(request,'dashboard/tambah_data.html')
  
  def post(self,request):
    data = {
      'nama_lengkap':request.POST.get('nama_lengkap'),
      'nik':request.POST.get('nik'),
      'nis':request.POST.get('nis'),
      'nisn':request.POST.get('nisn'),
      'tahun_lahir':request.POST.get('tahun_lahir'),
      'alamat_lengkap':request.POST.get('alamat_lengkap'),
      'kontak':request.POST.get('kontak') 
    }
    result = add_data_services(**data)
    
    if result.get('status'):
      messages.success(request,f'{result.get('messages')}')
      return redirect('dashboard_app:tambah_data')
    else:
      messages.error(request,f'{result.get('messages')}')
      return redirect('dashboard_app:tambah_data')
      