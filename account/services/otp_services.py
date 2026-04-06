from ..models import OTP 
from ..utils import hash_code,verify_code,generate_code
from django.contrib.auth.models import User

class OTPServices:
  
  @classmethod
  def create_otp(cls,user):
    code = generate_code()
    OTP.objects.create(
      user=user,
      hash_otp=hash_code(code)
      )
    return code
  
  def validate_otp(self,user_id,otp_input):
    try:
      user = User.objects.get(id=user_id)
      otp_obj = OTP.objects.get(user=user)
      
      if otp_obj.is_expired():
        otp_obj.delete()
        return {'status':False,'messages':'OTP IS EXPIRED'}
      
      if verify_code(otp_obj.hash_otp,otp_input):
        otp_obj.delete()
        return {'status':True,'messages':'OTP IS VALID'}
      else:
        return {'status':False,'messages':'OTP IS NOT VALID'}
    except OTP.DoesNotExist:
      return {'status':False,'messages':'OTP IS NOT FOUND'}
    except Exeption as e:
      return {'status':False,'messages':f"{e}"}
        
        
    
      
      