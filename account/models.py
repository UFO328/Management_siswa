from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class OTP(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  hash_otp = models.CharField(max_length=225)
  created_ad = models.DateTimeField(auto_now_add=True)
  
  def is_expired(self):
    return timezone.now() > self.created_ad + timedelta(minutes=5)