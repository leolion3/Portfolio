# RabbitMQ Connector Module

This module allows easily integrating RabbitMQ communication into your software.

## Requirements

The module requires the library `pika` to be installed. You can include it in your `requirements.txt` as

```
pika
```

## Setup

To use the module, simply import the `rabbit_messageio.py` file into your project.
To use the integrated logging, add
the [logger module from here](https://github.com/leolion3/Portfolio/tree/master/Python/Logger).

## Demo

The [`demo.py`](https://github.com/leolion3/Portfolio/blob/master/Python/RabbitMQConnector/demo.py) file demonstrates a
PING-REPLY
demo using the module. The RabbitMessageIO constructor takes as its arguments the RabbitMQ Host Address, the RabbitMQ
username and password.

It can be created using

```python
from rabbit_messageio import RabbitMessageIO

messageIO: RabbitMessageIO = RabbitMessageIO(
    host=rabbitmq_host,
    username=rabbitmq_username,
    password=rabbitmq_password
)
```

The messageIO object offers 3 api calls for running the send and receive channels:

1. `exec_send_channel(queues: List[str])`: Executes the channel for sending out messages. The messages can only be
   queued on the channels defined in the `queues` list.
2. `exec_recv_channel(queues: List[str], callback_function: Callable)`: Executes the receive channel, which listens on
   the registered queues and executes the callback function for incoming messages.
3. `exec(send_queues: List[str], recv_queues: List[str], callback_function: Callable)`: Starts an instance of each of
   the send and receive channels in parallel, each with their own queues.
   The channels run in separate threads indefinitely as daemon threads. Upon connection errors, they automatically
   attempt to reconnect.

The callback function needs to accept 4 parameters: channel, method, properties, body:

```python
def callback(channel, method, properties, body):
    """
    :param channel: Channel that the message was received from.
    :param method: Message method.
    :param properties: message properties from RabbitMQ.
    :param body: message body from RabbitMQ.
    """
    # To access the routing key (e.g. the RabbitMQ queue) use method.routing_key
```

For your applications, you probably want to use the `exec` method to handle incoming messages and send out new messages
from other parts of your software.

To queue messages **while the send thread is running**, you can use either one of

1. `queue_message(queue_key: str, message: any)`: Which queues a new message with any (JSON Serializable) content on the
   provided queue name. This queue needs to be registered for the send channel, see above.
2. `queue_dict(mdict: Dict[str, any])`: Like `queue_message`, allows queuing new messages but as a python dictionary.
   The dictionary must have the format:

```python
{
    'queue': 'RabbitMQ queue key (registered for the send channel)',
    'message': 'Any JSON Serializable content'
}
```

To queue a message from any part of your software, simply use `messageIO.queue_message` or `messageIO.queue_dict`. If
you want to make the process more straightforward
(instead of passing the `messageIO` around), you can remove the credentials from the `RabbitMessageIO` constructor
entirely and load them from an external configuration.

You can then add the singleton instance to the `rabbit_messageio` file and use it as such:

```python
    def __init__(self):
    """
    Default constructor.
    """
    logger.info('Setting up RabbitMQ MessageIO...', module=Module.RABBIT_IO)
    self.__credentials =  # Loaded from external config
    self.__rabbitmq_host:  # Loaded from external config
    self.__message_queue: queue = queue.Queue()
    logger.info('RabbitMQ Adapter initialized.', module=Module.RABBIT_IO)


singleton: RabbitMessageIO = RabbitMessageIO()
```

In other files you can then use the singleton instance:

```python
import rabbit_messageio
from rabbit_messageio import RabbitMessageIO

singleton: RabbitMessageIO = rabbit_messageio.singleton
singleton.queue_message() or singleton.queue_dict()
```

## Demo

The included [`demo.py` file](https://github.com/leolion3/Portfolio/blob/master/Python/RabbitMQConnector/demo.py)
implements a simple PING-REPLY demo using RabbitMQ.

To execute the demo, start the RabbitMQ server using the included `docker-compose.yml` file, then run the `demo.py`
file. The output will look similar to the following:

```bash
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:__init__:194 - [LOGGER] Initialising logger...
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:info:153 - [LOGGER] Logger initialized. 
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:info:153 - [RabbitMQ Message IO] Setting up RabbitMQ MessageIO... 
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:info:153 - [RabbitMQ Message IO] RabbitMQ Adapter initialized. 
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:info:153 - [RabbitMQ Message IO] Starting pika communication adapters... 
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:info:153 - [RabbitMQ Sender Thread] Starting send channel loop... 
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:info:153 - [RabbitMQ Receiver Thread] Starting receive channel loop... 
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:info:153 - [RabbitMQ Message IO] Connecting to RabbitMQ... 
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:info:153 - [RabbitMQ Message IO] Connecting to RabbitMQ... 
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:info:153 - [RabbitMQ Message IO] Connection successful. 
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:info:153 - [RabbitMQ Message IO] Connection successful. 
1970-01-01 00:00:00.001 | INFO     | log_handling.log_handler:info:153 - [RabbitMQ Receiver Thread] Registering queues ['ping-queue-ping', 'ping-queue-reply']
"PING"  # Queued message.
"PING"  # Queued dictionary.
"REPLY" # Response to queued message.
"REPLY" # Response to queued dictionary.
```

(\*) Note that the logs queuing the message are printed earlier than the messages. This is due to messages being
gradually sent out and received while being routed through the RabbitMQ server.
The communication is not instantaneous and has a delay of a couple ms.
