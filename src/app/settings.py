import os

NATS_SERVER = os.environ.get('NATS_SERVER')
JWT_TOKEN_ALGORITHM = 'HS256'
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')