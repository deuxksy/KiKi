#-*- coding: utf-8 -*-
import redis

from kiki import crypto
from kiki.config import config

redis_pool_common = redis.ConnectionPool(
    host=crypto.decrypt(config['db']['redis_host'].encode()).decode(),
    port=int(crypto.decrypt(config['db']['redis_port'].encode()).decode()),
    password=crypto.decrypt(config['db']['redis_password'].encode()).decode(),
    db=int(config['db']['redis_db_common']),
)
