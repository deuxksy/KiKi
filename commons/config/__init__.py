from configparser import ConfigParser
import pymysql

def get_config(file_path='config.ini'):
    parser = ConfigParser()
    parser.read(file_path)
    return parser


def get_config_db(config=None, db=None, cursorclass=pymysql.cursors.DictCursor):
    if config:
        db_config = {}
        db_config['host'] = config['db'][db + '.host']
        db_config['db'] = config['db'][db + '.db']
        db_config['user'] = config['db'][db + '.user']
        db_config['passwd'] = config['db'][db + '.passwd']
        db_config['charset'] = config['db'][db + '.charset']
        db_config['port'] = int(config['db'][db + '.port'])
        db_config['use_unicode'] = bool(config['db'][db + '.use_unicode'])
        if cursorclass:
            db_config['cursorclass'] = cursorclass
        return db_config
    return None


def get_default_config(file_path='config.ini', section=None):
    config = {}
    parser = ConfigParser()
    parser.read(file_path)
    if section:
        if (parser.has_section(section)):
            items = parser.items(section)
            for item in items:
                config[item[0]] = item[1]
    return config


def get_db_config(file_path='config.ini', section='db', cursorclass=pymysql.cursors.DictCursor, port=33061, use_unicode=True):
    config = get_default_config(file_path, section+'-oddsbox')
    if port:
        config['port'] = port
    if cursorclass:
        config['cursorclass'] = cursorclass
    if use_unicode:
        config['use_unicode'] = True
    return config


def get_webdrive_config(file_path='config.ini', section='db'):
    config = get_default_config(file_path, section+'-webdrive')
    return config