import redis
import falcon
import gevent
from random import uniform
from redis.exceptions import ResponseError

class DummyIngestionResource():
    
    def __init__(self):
        self.client = redis.Redis(host = '127.0.0.1', port = 9851, socket_keepalive=True, socket_timeout=60)
        self.client.execute_command('SETHOOK warehouse http://10.0.20.78/endpoint NEARBY fleet FENCE POINT 33.5123 -112.2693 500')     

    def on_post(self, req, resp):
        try:
            x1, y1 = uniform(-180,180), uniform(-90, 90)
            x2, y2 = uniform(-180,180), uniform(-90, 90)
            result1 = self.client.execute_command('SET', 'fleet', 'truck1', 'POINT', x1, y1)
            result2 = self.client.execute_command('SET', 'fleet', 'truck2', 'POINT', x2, y2)
            
            print result1
            print result2    
            print self.client.execute_command('GET', 'fleet', 'truck1')
            print self.client.execute_command('GET', 'fleet', 'truck2')      
            
            resp.status = falcon.HTTP_200
        except ResponseError:
            print('Error happened in the dummy client')
            resp.status = falcon.HTTP_400
