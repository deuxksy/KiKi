from kiki import redis_pool_common
import redis
import random
import json

def get_proxies():
    redis_common = redis.Redis(connection_pool=redis_pool_common)

    proxy_http = redis_common.lrange('proxy:http', 0, -1)
    proxy_https = redis_common.lrange('proxy:https', 0, -1)

    http = json.loads(proxy_http[random.randint(0, len(proxy_http) - 1)].decode('utf-8'))
    https = json.loads(proxy_https[random.randint(0, len(proxy_https) - 1)].decode('utf-8'))
    if http and https:
        return {
            'http':'http://{}:{}'.format(http.get('ip'), http.get('port')),
            'https':'http://{}:{}'.format(https.get('ip'), https.get('port')),
        }
    else:
        return None