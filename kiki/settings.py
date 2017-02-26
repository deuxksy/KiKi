import redis

from kiki import crypto
from kiki.config import config

redis_pool_common = redis.ConnectionPool(
    host=crypto.decrypt(config['db']['redis.host'].encode()).decode(),
    port=int(crypto.decrypt(config['db']['redis.port'].encode()).decode()),
    password=crypto.decrypt(config['db']['redis.password'].encode()).decode(),
    db=int(config['db']['redis.db.common']),
)
