#
# -*- encoding: utf-8 -*-

import redis

""""""
conn = redis.Redis()

# 如果用户对一个不存在的键或者一个保存了空串的键执行自增或者自减操作， 那么Redis在执行操作时会将这个key的值当作0来处理。
conn.get('key')
conn.incr('key')
conn.incr('key', 15)
conn.decr('key', 5)
conn.pipeline()

