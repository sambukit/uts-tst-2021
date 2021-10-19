import jwt
from decouple import config

import time
from typing import Dict

JWT_SECRET = config("kunci")
JWT_ALGORITHM = config("algo")

def tokenresponse(token: str):
    return{
        "token_akses": token
    }

def signJWT(userID: str) -> Dict[str,str]:
    payload = {
        "userID" : userID
        "masaberlaku" : time.time() + 3600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return tokenresponse(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["masaberlaku"] >= time.time() else None
    except:
        return {}
