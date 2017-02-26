import os
from configparser import ConfigParser

import redis
from cryptography.fernet import Fernet

__version__ = (0, 0, 1)

crypto = Fernet(os.getenv('ZZIZILY_KIKI_CRYPTO'))

config = ConfigParser()
config.read('./resources/{mode}_config.ini'.format(mode=os.getenv('ZZIZILY_KIKI_MODE')))

redis_pool_common = redis.ConnectionPool(
    host=crypto.decrypt(config.get('db', 'redis.host').encode()).decode(),
    port=int(crypto.decrypt(config.get('db', 'redis.port').encode()).decode()),
    password=crypto.decrypt(config.get('db', 'redis.password').encode()).decode(),
    db=int(config.get('db', 'redis.db.common')),
)