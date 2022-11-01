import time
from typing import Dict
import jwt
from decouple import config
import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.environ['JWT_SECRET_KEY'] 
JWT_ALGORITHM = os.environ['JWT_ALGORITHM'] 

def token_response(token: str):
    return{
        "access_token": token,
    }

def signJWT(user_id, username, role):
    payload = {
        "user_id": user_id,
        "user_name": username,
        "role":"role",
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)

def decodeJWT(token):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}