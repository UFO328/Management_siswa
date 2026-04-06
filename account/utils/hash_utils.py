from argon2 import PasswordHasher

ph = PasswordHasher()

#fuction for hash code otp 
def hash_code(code):
  return ph.hash(code)

#function for verify code 
def verify_code(hash_code,code):
  return ph.verify(hash_code,code)