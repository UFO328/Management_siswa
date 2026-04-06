from django.urls import path 
from .views import DashboardView,ViewAddData,ListViewSiswa,UpdateSiswa

app_name = 'dashboard_app'

urlpatterns = [
  path('',DashboardView.as_view(),name='dashboard'),
  path('tambah_data/',ViewAddData.as_view(),name='tambah_data'),
  path('list_data/',ListViewSiswa.as_view(),name='list_data'),
  path('update_data/<int:id>/',UpdateSiswa,name='update_data'),
  ]