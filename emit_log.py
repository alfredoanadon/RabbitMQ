#!/usr/bin/env python
import pika
import sys

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

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()