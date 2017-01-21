import psycopg2
import psycopg2.extras


def get_postgresql(config=None, db=None, cursorclass=psycopg2.extras.DictCursor):
    return psycopg2.connect(dbname=config['db'][db + '.dbname'], user=config['db'][db + '.user'], host=config['db'][db + '.host'], password=config['db'][db + '.password'],cursor_factory=psycopg2.extras.DictCursor)