#!/usr/bin/env python3
"""
Open-Source RabbitMQ Connector Module by Leonard Haddad, 2025.
Provided in accords with the MIT License.
More on GitHub at https://leolion.tk/
"""
import json
import queue
import time
from threading import Thread
from typing import List, Dict, Callable

import pika as pika
from log_handling import log_handler
from log_handling.log_handler import Logger, Module
from pika.adapters.blocking_connection import BlockingChannel

logger: Logger = log_handler.get_instance()


class RabbitMessageIO:
    """
    Handles rabbitmq communication.
    """

    def queue_dict(self, mdict: Dict[str, any]) -> None:
        """
        Allows queuing messages as a dictionary.
        :param mdict: the dictionary in the format {'queue':..., 'message':....}
        :return:
        """
        if 'queue' not in mdict.keys():
            logger.error(f"Tried queuing a packet \"{mdict}\" but it didn't contain an 'queue' key.",
                         module=Module.RABBIT_IO)
            return
        if 'message' not in mdict.keys():
            logger.error(f"Tried queuing a packet \"{mdict}\" but it didn't contain a 'message' key.",
                         module=Module.RABBIT_IO)
            return
        self.__message_queue.put(mdict)
        logger.debug(f'Queued new message \"{mdict}\".', module=Module.RABBIT_IO)

    def queue_message(self, queue_key: str, message: any) -> None:
        """
        Add a new message to the queue from the receiver thread (hence the locking).
        :param queue_key: key for identifying the rabbitMQ message.
        :param message: the message to queue. Needs to be JSON serializable.
        :return:
        """
        mdict: Dict[str, any] = {
            'queue': queue_key,
            'message': message
        }
        self.__message_queue.put(mdict)
        logger.debug(f'Queued new message \"{mdict}\".', module=Module.RABBIT_IO)

    def _connect(
            self,
            retries=0
    ) -> BlockingChannel:
        """
        Attempts to connect to the rabbitMQ host and returns the channel object.
        :param retries: how often the connection was retried.
        :return: the rabbitMQ channel object.
        """
        try:
            logger.info('Connecting to RabbitMQ...', module=Module.RABBIT_IO)
            connection: pika.BlockingConnection = pika.BlockingConnection(
                pika.ConnectionParameters(self.__rabbitmq_host, 5672, '/', self.__credentials, heartbeat=0))
            logger.info('Connection successful.', module=Module.RABBIT_IO)
            return connection.channel()
        except Exception as e:
            if retries >= 3:
                logger.error('No successful connection after 3 tries. Trace:', e, module=Module.RABBIT_IO)
                raise
            logger.error(f'RabbitMQ connection failed. Retrying in 1 second ({retries + 1}/3)...',
                         module=Module.RABBIT_IO)
            time.sleep(1)
            return self._connect(retries=retries + 1)

    def __check_for_messages(self, __send_channel: BlockingChannel) -> None:
        """
        Sends out all messages from the massage queue.
        :return:
        """
        item = self.__message_queue.get()
        _queue: str = item.get('queue')
        message: any = item.get('message')
        if not _queue or not message:
            logger.error('Malformed message. Queue or message was None.', module=Module.RABBIT_SEND)
            return
        self.__produce(__send_channel, _queue, message)
        logger.debug(f'Sent message \"{_queue}\": \"{message}\"', module=Module.RABBIT_SEND)

    def __produce(self, __send_channel: BlockingChannel, _queue, message_body, retries=0) -> None:
        """
        Sends data to rabbitMQ.
        :return:
        """
        try:
            __send_channel.basic_publish(
                exchange='',
                body=json.dumps(message_body).encode('utf-8'),
                routing_key=_queue
            )
        except Exception as e:
            if retries >= 3:
                logger.error(f'Error sending message \"{_queue}\":\"{message_body}\". Skipping. Trace: {e}...',
                             module=Module.RABBIT_SEND)
                return
            logger.error(f'Error sending message \"{_queue}\":\"{message_body}\". Retrying {retries + 1}/3...',
                         module=Module.RABBIT_SEND)
            self.__produce(__send_channel, _queue, message_body, retries + 1)

    def __init_send_channel(self, queues: List[str]) -> BlockingChannel:
        """
        Initialises the pika communication channel for sending messages.
        :param queues: RabbitMQ queues to register for the send thread.
        :return: the pika communication channel.
        """
        channel: BlockingChannel = self._connect()
        for _queue in queues:
            channel.queue_declare(queue=_queue)
        return channel

    def __init_recv_channel(self, queues: List[str], callback_function: Callable) -> BlockingChannel:
        """
        Initialises the pika communication channel for receiving messages.
        :param queues: The RabbitMQ queues to register for the receiver channel.
        :param callback_function: function to call when message is received. Needs to accept 4 parameters.
        :return: the pika communication channel.
        """
        channel: BlockingChannel = self._connect()
        logger.info('Registering queues', queues, module=Module.RABBIT_RECV)
        for _queue in queues:
            channel.queue_declare(queue=_queue)
            channel.basic_consume(queue=_queue, auto_ack=True, on_message_callback=callback_function)
        return channel

    def exec_send_channel(self, queues: List[str]) -> None:
        """
        Handles outgoing rabbitMQ messages.
        :param queues: The RabbitMQ queues to register for the sender channel.
        :return:
        """
        while True:
            try:
                logger.info('Starting send channel loop...', module=Module.RABBIT_SEND)
                send_channel: BlockingChannel = self.__init_send_channel(queues=queues)
                while True:
                    self.__check_for_messages(send_channel)
            except Exception as e:
                logger.error(f'Send channel crashed. Trace: {e}. Restarting...', module=Module.RABBIT_SEND)

    def exec_recv_channel(self, queues: List[str], callback_function: Callable) -> None:
        """
        Handles incoming rabbitMQ messages.
        :param queues: The RabbitMQ queues to register for the receiver channel.
        :param callback_function: function to call when message is received. Needs to accept 4 parameters.
        :return:
        """
        while True:
            try:
                logger.info('Starting receive channel loop...', module=Module.RABBIT_RECV)
                recv_channel: BlockingChannel = self.__init_recv_channel(
                    queues=queues,
                    callback_function=callback_function
                )
                recv_channel.start_consuming()
            except Exception as e:
                logger.error(f'Receive channel crashed. Trace: {e}. Restarting...', module=Module.RABBIT_RECV)

    def exec(self, send_queues: List[str], recv_queues: List[str], callback_function: Callable) -> None:
        """
        Receives data using pika from rabbitMQ, passes the request to the psu and sends out a response.
        This is the rabbitMQ thread's main loop and should never stop.
        :param send_queues: The RabbitMQ queues to register for the sender channel.
        :param recv_queues: The RabbitMQ queues to register for the receiver channel.
        :param callback_function: function to call when message is received. Needs to accept 4 parameters.
        :return:
        """
        logger.info('Starting pika communication adapters...', module=Module.RABBIT_IO)
        send_thread: Thread = Thread(target=self.exec_send_channel, args=(send_queues,), daemon=True)
        recv_thread: Thread = Thread(target=self.exec_recv_channel, args=(recv_queues, callback_function), daemon=True)
        threads: List[Thread] = [send_thread, recv_thread]
        [t.start() for t in threads]

    @staticmethod
    def __validate_credentials(host: str, username: str, password: str) -> bool:
        """
        Validates the rabbitMQ credentials before using them.
        :param host: the rabbitMQ host address.
        :param username: the rabbitMQ username.
        :param password: the rabbitMQ password.
        :return: True if the credentials are valid, False otherwise.
        """
        for item in [host, username, password]:
            if item is None or not item or not len(item.strip()):
                return False
        return True

    def __init__(self, host: str, username: str, password: str):
        """
        Default constructor.
        :param host: the rabbitMQ host address.
        :param username: the rabbitMQ username.
        :param password: the rabbitMQ password.
        """
        logger.info('Setting up RabbitMQ MessageIO...', module=Module.RABBIT_IO)
        if not self.__validate_credentials(host, username, password):
            raise Exception('Invalid or missing credentials for RabbitMQ.')
        self.__credentials = pika.PlainCredentials(username, password)
        self.__rabbitmq_host: str = host
        self.__message_queue: queue = queue.Queue()
        logger.info('RabbitMQ Adapter initialized.', module=Module.RABBIT_IO)
