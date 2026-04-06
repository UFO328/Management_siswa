from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from django.contrib import messages 
from django.views import View  
from ..services import OTPServices,send_services
from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from django.contrib.auth.decorators import login_required 

class RegisterAuthSytem(View):
  def get(self,request):
    return render(request,'account/register.html')
  
  def post(self,request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
      messages.error(request,'DATA TIDAK VALID GUNAKAN USERNAME ATAU EMAIL LAIN')
      return redirect('account_app:register')
    if confirm_password != password:
      messages.error(request,'PASSWORD TIDAK SAMA')
      return redirect('account_app:register')
      
    user = User.objects.create_user(
      first_name=first_name,
      last_name=last_name,
      email=email,
      username=username,
      password=password,
      is_active=False
      
      )
    request.session['user_id'] = user.id
    otp = OTPServices.create_otp(user)
    send_services(user,otp)
    return redirect('account_app:verifikasi_otp')

class LoginAuthSytem(View):
  def get(self,request):
    return render(request,'account/login.html')
  
  def post(self,request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user and user.is_active:
        login(request, user)
        return redirect('dashboard_app:dashboard')
    else:
      messages.error(request,'USERNAME OR PASSWORD IS WRONG')
      return redirect('account_app:login')

@login_required
def logout_user(request):
  logout(request)
  return redirect(settings.LOGOUT_REDIRECT_URL)