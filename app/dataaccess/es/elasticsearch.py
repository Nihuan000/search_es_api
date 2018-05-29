# -*- coding: utf-8 -*-
"""
 * Created by PyCharm.
 * User: nihuan
 * Date: 18-5-29
 * Time: 下午9:53
 * Desc: 
 """
__author__ = 'nihuan'

from elasticsearch import Elasticsearch
from app import config


class ApiEs(object):
    def __init__(self):
        es_conf = config.ES_CONFIG
        self.es = Elasticsearch(hosts=[{'host': es_conf['es_host'], 'port': es_conf['es_port']}],
                                http_auth=(es_conf['es_user'], es_conf['es_password']))

    def search(self, params):
        res = self.es.search()

    def get_index(self):
        res = self.es.get()

    def get_info(self):
        res = self.es.info()
        print(res)
