from kombu import Connection, Exchange, Producer, Queue

rabbit_url = 'amqp://guest:guest@localhost:5672//'

conn = Connection(rabbit_url)

channel = conn.channel()

exchange = Exchange('tile38_experiment', type='topic')

producer = Producer(exchange=exchange, channel=channel)

queue = Queue(name='tile38_geo_experiment', exchange=exchange)

queue.maybe_bind(conn)

queue.declare()

producer.publish('Hello there')
