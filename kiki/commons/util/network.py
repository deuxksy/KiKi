import requests


def get_ip():
    return requests.get('http://ifconfig.co/json').json().get('ip')
