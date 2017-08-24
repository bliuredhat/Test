##
##
import time
import json

def check_token(conn, token):
    return conn.hget('login:', token)

def update_token(conn, token, user, item=None):
    timestamp = time.time()
    conn.hset('login:', token, user)
    conn.zadd('recent:', token, timestamp)
    if item:
        conn.zadd('viewed:' + token, item, timestamp)
        conn.zremrangebyrank('viewed:' + token, 0, -26)

#***********************************************************
QUIT = False
LIMIT = 10000000

def clean_sessions(conn):
    while not QUIT:
        size = conn.zcard('recent:')
        if size <= LIMIT:
            time,sleep(1)
            continue

        end_index = min(size - LIMIT, 100)
        tokens = conn.zrange('recent:', 0, end_index-1)
        session_key = []
        for token in tokens:
            session_key.append(*session_keys)

        conn.delete(*session_keys)
        conn.hdel('login:', *tokens)
        conn.hdel('recent:', *tokens)

#****************************************************************
def add_to_cart(conn, session, item, count):
    if count <=0:
        conn.hrem('cart:' + session, item)
    else:
        conn.hset('cart:' + session, item, count)

def clean_full_sessions(conn):
    while not QUIT:
        size = conn.zcard('recent:')
        if size <= LIMIT:
            time.sleep(1)
            continue
        end_index = min(size - LIMIT, 100)
        sessions = conn.zrange('recent:', 0, end_index-1)
        session_keys = []
        for sess in sessions:
            session_keys.append('viewed:' + sess)
            session_keys.append('cart:' + sess)

        conn.delete(*session_keys)
        conn.hdel('login:', *sessions)
        conn.zrem('recent:', *sessions)

def cache_request(conn, request, callback):
    if not can_cache(conn, request):
        return callback(request)

    page_key = 'cache:' + hash_request(request)
    content = conn.get(page_key)
    if not content:
        content = callback(request)
        conn.setex(page_key, content, 300)

    return content

def schedule_row_cache(conn, row_id, delay):
    conn.zadd('deplay:', row_id, delay)
    conn.zadd('schedule:', row_id, time.time())

def cache_rows(conn):
    while not QUIT:
        next = conn.zrange('schedule:', 0, 0, withscores=True)
        now = time.time()
        if not next or next[0][1] > now:
            time.sleep(.05)
            continue

        row_id = next[0][0]
        delay = conn.zscore('deplay:', row_id)
        if delay <= 0:
            conn.zrem('deplay:', row_id)
            conn.zrem('schedule:', row_id)
            conn.delete('inv:' + row_id)
            continue

        """
        row = Inventory.get(row_id)    #*************
        conn.zadd('schedule:', row_id, now + delay)
        conn.set('inv:' + row_id, json.dumps(row.to_dict()))
        """

def update_token(conn, token, user, item=None):
    timestamp = time.time()
    conn.hset('login:', token, user)
    conn.zadd('recent:', token, user)
    if item:
        conn.zadd('viewed:' + token, item, timestamp)
        conn.zremrangebyrank('viewed:' + token, 0, -26)
        conn.zincrby('viewed:', item, -1)

def rescale_viewed(conn):
    while not QUIT:
        conn.zremrangebyrank('viewed:', 0, -20001)
        conn.zinterstore('viewed:', {'viewed:' .5})
        time.sleep(30)

def can_cache(conn, request):
    """
    item_id = extract_item_id(request)   #*************

    if not item_id or is_dynamic(request):
        return  False

    rank = conn.zrank('viewed:', item_id)
    return rank is not None and rank < 1000
    """
    pass
