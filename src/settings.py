from cryptography.fernet import Fernet
from configparser import ConfigParser
import redis
import os

__version__ = (0, 0, 1)

crypto = Fernet(os.getenv('ZZIZILY_KIKI_CRYPTO'))

config = ConfigParser()
config.read(os.getenv('ZZIZILY_KIKI_CONFIG'))

redis_pool_common = redis.ConnectionPool(
    host=crypto.decrypt(config.get('db', 'redis.host').encode()).decode(),
    port=int(crypto.decrypt(config.get('db', 'redis.port').encode()).decode()),
    password=crypto.decrypt(config.get('db', 'redis.password').encode()).decode(),
    db=int(config.get('db', 'redis.db.common')),
)