import os

import redis
from cryptography.fernet import Fernet

from kiki.config import config

crypto = Fernet(os.getenv('ZZIZILY_KIKI_CRYPTO'))
redis_pool_common = redis.ConnectionPool(
    host=crypto.decrypt(config['db']['redis.host'].encode()).decode(),
    port=int(crypto.decrypt(config['db']['redis.port'].encode()).decode()),
    password=crypto.decrypt(config['db']['redis.password'].encode()).decode(),
    db=int(config['db']['redis.db.common']),
)
