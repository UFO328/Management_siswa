from django.shortcuts import render,redirect 
from django.views import View 
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin,View):
  def get(self,request):
    return render(request,'dashboard/dashboard.html')
  