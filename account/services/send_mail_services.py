from django.core.mail import send_mail
from django.conf import settings

def send_services(user,otp):
    send_mail(
        'Register Verification',          # Subjek
        f'This Your OTP {otp} Not Share To Another People', # Isi pesan (body)
        settings.DEFAULT_FROM_EMAIL,  # Email pengirim (dari settings.py)
        [user.email],       # Daftar email penerima (harus dalam list [])
        fail_silently=False,          # Jika True, error tidak akan muncul kalau gagal
    )
