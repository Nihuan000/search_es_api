# -*- coding: utf-8 -*-
"""
 * Created by PyCharm.
 * User: nihuan
 * Date: 18-5-29
 * Time: 下午5:40
 * Desc: 
 """
__author__ = 'nihuan'

import os
import configparser


BRAND_NAME = 'Elasticsearch REST API'

SECRET_KEY = 'xs4G5ZD9SwNME6nWRWrK_aq6Yb9H8VJpdwCzkTErFPw='
UUID_LEN = 10
UUID_ALPHABET = ''.join(map(chr, range(48, 58)))
TOKEN_EXPIRES = 3600

APP_ENV_PATH = open(os.path.dirname(__file__) + '/../.ENV')
APP_ENV = APP_ENV_PATH.read()
INI_FILE = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '../conf/{}.ini'.format(APP_ENV))

CONFIG = configparser.ConfigParser()
CONFIG.read(INI_FILE)

if APP_ENV == 'dev' or APP_ENV == 'online' or APP_ENV == 'test':
    DB_CONFIG = CONFIG['app_db']
    SEARCH_CONFIG = CONFIG['es_db']
    ES_CONFIG = CONFIG['elasticsearch']
    REDIS_CONFIG = CONFIG['redis']
    GETUI_CONFIG = CONFIG['getui']
    MALONG_CONFIG = CONFIG['malong']
else:
    exit('获取不到运行环境状态')

DB_ECHO = True if CONFIG['database']['echo'] == 'yes' else False
DB_AUTOCOMMIT = True

LOG_LEVEL = CONFIG['logging']['level']
