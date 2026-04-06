from django.urls import path 
from .views import RegisterAuthSytem,LoginAuthSytem,VerifyOtp,logout_user

app_name = 'account_app'

urlpatterns = [
  path('',LoginAuthSytem.as_view(),name='login'),
  path('register/',RegisterAuthSytem.as_view(),name='register'),
  path('verifikasi_otp/',VerifyOtp.as_view(),name='verifikasi_otp'),
  path('logout/',logout_user,name='logout'),
  ]