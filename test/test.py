# -*- coding: utf-8 -*-
"""
 * Created by PyCharm.
 * User: nihuan
 * Date: 18-5-29
 * Time: 下午10:06
 * Desc: 
 """
__author__ = 'nihuan'

from app.dataaccess.es.elasticsearch import ApiEs
from app.dataaccess.mysql.mysql import AppDb
import time

start = time.time()
es_cluser = ApiEs()
es_cluser.get_info()

db = AppDb()
db.get_db_info()

end = time.time()
print(end - start)
