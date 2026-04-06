from django.views.generic import ListView 
from ..models import Siswa 

class ListViewSiswa(ListView):
  model = Siswa
  template_name = 'dashboard/list_siswa.html'
  context_object_name = 'siswa_list'
  ordering = ['id']
  paginate_by = 5