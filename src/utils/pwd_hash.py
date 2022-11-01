import bcrypt
import os

def get_hashed_password(password):
   #bytePwd = password.encode('utf-8')
   hash= bcrypt.hashpw(password = password.encode('utf8'), salt = bcrypt.gensalt())
   return hash.decode('utf8')

def  verify_password(password, hash):
   return bcrypt.checkpw(password.encode('utf8'), hash.encode('utf8'))