from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from django.contrib import messages 
from django.views import View  
from ..services import OTPServices


class VerifyOtp(View):
  def get(self,request):
    if not request.session['user_id']:
      return redirect('account_app:register')
    return render(request,'account/verifikasi_otp.html')
  
  def post(self, request):
    try:
        user_id = request.session.get('user_id')

        if not user_id:
            messages.error(request, "Session expired")
            return redirect('account_app:register')

        user = User.objects.get(id=user_id)
        otp_input = request.POST.get('otp')

        if not otp_input:
            messages.error(request, "OTP wajib diisi")
            return redirect('account_app:verifikasi_otp')

        otp_obj = OTPServices()
        otp_validasi = otp_obj.validate_otp(user_id,otp_input)

        if otp_validasi.get('status'):
            messages.success(request, f"{otp_validasi.get('messages')}")

            user.is_active = True
            user.save()

            del request.session['user_id']

            return redirect('account_app:login')

        else:
            messages.error(request, f"{otp_validasi.get('messages')}")
            return redirect('account_app:verifikasi_otp')

    except User.DoesNotExist:
        messages.error(request, "USER NOT FOUND")
        return redirect('account_app:register')
