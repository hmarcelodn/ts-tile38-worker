from kombu import Connection, Exchange, Queue
from kombu.mixins import ConsumerMixin
from random import uniform
from redis.exceptions import ResponseError
import redis

class Worker(ConsumerMixin):
    exchange = Exchange('tile38_experiment', type='topic')
    q = Queue(exchange=exchange, exclusive=True)

    def __init__(self, connection):
        self.connection = connection
        self.client = redis.Redis(host = '127.0.0.1', port = 9851)

    def get_consumers(self, Consumer, channel):
        print('get_consumers')
        return [Consumer(queues=[self.q], callbacks=[self.on_task])]

    def on_task(self, body, message):
        print('on_task')
        try:
            x1, y1 = uniform(-180,180), uniform(-90, 90)
            x2, y2 = uniform(-180,180), uniform(-90, 90)
            result1 = self.client.execute_command('SET', 'fleet', 'truck1', 'POINT', x1, y1)
            result2 = self.client.execute_command('SET', 'fleet', 'truck2', 'POINT', x2, y2)
            
            print(result1)
            print(result2)   
            print(self.client.execute_command('GET', 'fleet', 'truck1'))
            print(self.client.execute_command('GET', 'fleet', 'truck2'))     
            
            #message.ack()
        except ResponseError:
            print('Error happened in the dummy client')
       
        message.ack()


if __name__ == '__main__':
    print('Initilize worker...')
    with Connection('amqp://guest:guest@localhost:5672//') as conn:
        worker = Worker(conn)
        worker.run()
    print('Worker is initialized')