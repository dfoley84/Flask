import pika
import json


def RabbitMQ_Delete_VDesk(*data):
    for i in data:
        message = {'HorizonServer': i[0], 'PoolName': i[1], 'Machine': i[2] }
    try:
        print(message)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='')) 
        channel = connection.channel()
        channel.queue_declare(queue='DeleteMachine')
        channel.basic_publish(exchange='',
                                routing_key='DeleteMachine',
                                body=json.dumps(message),
                                properties=pika.BasicProperties(
                                    delivery_mode=2,
                                ))
        connection.close()
    except pika.exceptions.AMQPChannelError as err:
        print("Caught a channel error: {}, stopping...".format(err))
        
