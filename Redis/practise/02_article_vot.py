#
#

import time
import redis

hostname =  '127.0.0.1'
port = 6379

conn = redis.Redis(host=hostname,
                   port=port,
                   )

ONE_WEEK_IN_SECOND = 7 * 86400
VOTE_SCORE = 432

def artical_vot(conn, user, article):
    cutoff = time.time() - ONE_WEEK_IN_SECOND
    if conn.zscroe('time:', article) < cutoff:
        return

    article_id = article.partition(':')[-1]
    if conn.sadd('voted:' + article_id, user):         #
        conn.zincrby('score:', article, VOTE_SCORE)
        conn.hincrby(article, 'votes', 1)

#***************************************************************

def post_article(conn, user, title, link):
    article_id = str(conn.incr('article:'))

    voted = 'voted:' + article_id
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECOND)

    now = time.time()
    article = 'article:' + article_id
    conn.hmset(article, {
        'title': title,
        'link': link,
        'poster': user,
        'time': now,
        'votes': 1,
    })

    conn.zadd('score:', article, now + VOTE_SCORE)
    conn.zadd('time:', article, now)

    return article_id

#***************************************************************
ARTICLES_PER_PAGE = 25

def get_articles(conn, page, order='score:'):
    start = (page-1) * ARTICLES_PER_PAGE
    end = start + ARTICLES_PER_PAGE -1

    ids = conn.zrevrange(order, start, end)
    articles = []
    for id in ids:
        article_data = conn.hgetall(id)
        article_data['id'] = id
        articles.append(article_data)

    return articles

#****************************************************************
def add_remove_groups(conn, article_id, to_add=[], to_remove=[]):
    article = 'article' + article_id
    for group in to_add:
        conn.sadd('group:' + group, article)
    for group in to_remove:
        conn.srem('group:' + group, article)

#****************************************************************
def get_group_article(conn, group, page, order='score:'):
    key = order + group
    if not conn.exists(key):
        conn.zinterstore(key,
                         ['group:' + group, order],
                         aggregate='max',
                         )
        conn.expire(key, 60)

    return get_articles(conn, page, key)
