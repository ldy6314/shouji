import jwt
from datetime import datetime, timedelta

SECRET_KEY = b'\x92\x8e\xc6\x9c\xb3\x89\xa6\x0c\xcb\xf6\xcb\xd7\xbc'


def generate_token(userid=0, algorithm='HS256', exp=2, key=SECRET_KEY):
    now = datetime.utcnow()
    exp_int = now + timedelta(hours=exp)
    payload = {
        'exp': exp_int,
        'flag': 0,
        'iat': now,
        'iss': 'ldy',
        'userid': userid
    }
    token = jwt.encode(payload, key, algorithm)
    return token


def decode_token(token, key=SECRET_KEY, algorithm='HS256'):
    try:
        payload = jwt.decode(token, key, algorithm)
    except jwt.ExpiredSignatureError:
        return 0, '签名过期'
    except jwt.InvalidTokenError:
        return 0, '令牌不合法'
    except jwt.InvalidSignatureError:
        return 0, '签名不合法'
    else:
        return 1, payload





