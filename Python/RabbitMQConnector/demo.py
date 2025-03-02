#!/usr/bin/env python3
"""
Simple Ping-Reply demo script to showcase the RabbitMQ module.
"""
import time
from typing import List

from rabbit_messageio import RabbitMessageIO

rabbitmq_host: str = 'localhost'
rabbitmq_username: str = 'guest'
rabbitmq_password: str = 'guest'
messageIO: RabbitMessageIO = RabbitMessageIO(
    host=rabbitmq_host,
    username=rabbitmq_username,
    password=rabbitmq_password
)


def callback(channel, method, properties, body):
    """
    Callback for handling the incoming RabbitMQ message.
    :param channel: Channel that the message was received from.
    :param method: Message method.
    :param properties: message properties from RabbitMQ.
    :param body: message body from RabbitMQ.
    :return:
    """
    global messageIO
    if method.routing_key == 'ping-queue-ping':
        print(body.decode('utf-8'))
        messageIO.queue_message('ping-queue-reply', 'REPLY')
    elif method.routing_key == 'ping-queue-reply':
        print(body.decode('utf-8'))


if __name__ == '__main__':
    # For demo purposes, register same queues for send and receive channels.
    queues: List[str] = ['ping-queue-ping', 'ping-queue-reply']
    messageIO.exec(
        send_queues=queues,
        recv_queues=queues,
        callback_function=callback
    )
    # Queue new messages. Messages are sent out gradually, not instantaneously.
    messageIO.queue_message('ping-queue-ping', 'PING')
    messageIO.queue_dict({
        'queue': 'ping-queue-ping',
        'message': 'PING'
    })
    # Allow RabbitMQ messages to be sent out and received.
    time.sleep(60)
