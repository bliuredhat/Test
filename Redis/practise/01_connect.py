
import redis

hostname =  '127.0.0.1'
port = 6379

conn = redis.Redis(host=hostname,
                   port=port,
                   )
conn.set('foo', 'bar')
value = conn.get('foo')
print "The value is: %s" % value