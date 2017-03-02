#-*- coding: utf-8 -*-
import requests
from requests.exceptions import ProxyError


def get_ip(proxies=None):
    ip = None
    try:
        ip = requests.get('https://ifconfig.co/json', proxies=proxies).json().get('ip')
    except ProxyError:
        ip = requests.get('https://ifconfig.co/json', proxies=proxies).json().get('ip')
    finally:
        return ip