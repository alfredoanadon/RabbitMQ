import pika

#connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.56.1'))
#channel = connection.channel()

credentials = pika.PlainCredentials('linux', 'linux')
parameters = pika.ConnectionParameters('aaaa',
                                       5672,
                                       'linux',
                                       credentials) ## localhost --ip mv

##connection =  pika.BlockingConnection(parameters)
connection = pika.BlockingConnection(parameters)

##connection = pika.BlockingConnection(pika.ConnectionParameters(host='guest'))
channel = connection.channel()


channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body.decode("utf-8"))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()