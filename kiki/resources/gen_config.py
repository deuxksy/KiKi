import argparse
import os
import sys
from datetime import datetime

from kiki.settings import crypto


def args():
    try:
        parser = argparse.ArgumentParser(description='default argument')
        parser.add_argument('-m', '--mode', type=str, help='배포할 모드를 선택해 주세요 (local, dev, prod)', required=True)
        return parser.parse_args()
    except:
        sys.exit(1)


if __name__ == '__main__':
    param = args()

    properties = [
        {'key': '[default]'},
        {'key': 'mode', 'value': param.mode},

        {'key': '[telegram]'},
        {'key': 'token', 'value': telegram_token.decode()},
        {'key': 'chat_id', 'value': telegram_chat_id.decode()},

        {'key': '[slack]'},
        {'key': 'token', 'value': slack_token.decode()},
        {'key': 'channel', 'value': '#carpediem'},
        {'key': 'username', 'value': 'carpediem'},

        {'key': '[db]'},
        {'key': 'redis.host', 'value': redis_host.decode()},
        {'key': 'redis.port', 'value': redis_port.decode()},
        {'key': 'redis.password', 'value': redis_password.decode()},
        {'key': 'redis.db.common', 'value': 0},

        {'key': '[log]'},
        {'key': 'path', 'value': 'D:\DK\Version\Git\ZZiZiLY\Python\Kkiki\log'},
        {'key': 'prefix', 'value': '%%Y/%%m/%%d'},
        {'key': 'suffix', 'value': '%%H%%M%%S'},
        {'key': 'formatter', 'value': '[%%(levelname)s|%%(filename)s:%%(lineno)s] %%(asctime)s > %%(message)s'},
        {'key': 'file.size', 'value': 128},
        {'key': 'encoding', 'value': 'utf-8'},
    ]

    if os.path.exists('./{mode}_config.ini'.format(mode=param.mode)):
        os.rename('./{mode}_config.ini'.format(mode=param.mode),
                  './{mode}_config.old.{datetime}.ini'.format(mode=param.mode,
                                                              datetime=datetime.today().strftime('%y%m%d%H%M%S')))

    with open('./{mode}_config.ini'.format(mode=param.mode), 'w') as f:
        for i, property in enumerate(properties):
            if None is property.get('value'):
                if i == 0:
                    f.write('{key}\n'.format(key=property.get('key')))
                else:
                    f.write('\n{key}\n'.format(key=property.get('key')))
            elif None is not property.get('value'):
                f.write('{key}={value}\n'.format(key=property.get('key'), value=property.get('value')))
    f.close()
