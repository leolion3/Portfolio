#!/usr/bin/env python3
"""
Open-Source thread-safe queue module by Leonard Haddad, 2025.
Provided in accords with the MIT License.
More on GitHub at https://leolion.tk/
"""
import threading
from copy import deepcopy
from typing import List, Any, Optional


class ThreadSafeQueue:
    """
    Implements a thread-safe queue using lists with contains and size operations.
    """

    def __init__(self):
        """
        Default constructor.
        """
        self._queue: List[Any] = []
        self._queue_lock = threading.Lock()
        self._not_empty = threading.Condition(self._queue_lock)

    def get_queue(self) -> List[Any]:
        """
        Get a snapshot of the current queue (unreliable).
        :return: A snapshot of the queue.
        """
        with self._queue_lock:
            return deepcopy(self._queue)

    def contains(self, elem: Any) -> bool:
        """
        Check if the given item is in the queue.
        :param elem: The item to check.
        :return: True if the item is in the queue, False otherwise.
        """
        with self._queue_lock:
            return elem in self._queue

    def size(self) -> int:
        """
        Return current size of the queue (unreliable).
        :return: current size of the queue.
        """
        with self._queue_lock:
            return len(self._queue)

    def delete(self, elem: Any) -> bool:
        """
        Removes the given item from the queue.
        :param elem: Item to remove.
        :return: True if the item was removed, False otherwise.
        """
        with self._queue_lock:
            if elem in self._queue:
                self._queue.remove(elem)
                return True
            return False

    def pop(self, timeout: float = 30) -> Optional[Any]:
        """
        Pops the first element of the queue (blocking).
        :param timeout: max timeout (in seconds) to wait before terminating. Can be None for wait-forever.
        :return: The first element of the queue (FIFO).
        """
        with self._not_empty:
            if not self._queue:
                notified: bool = self._not_empty.wait(timeout=timeout)
                if not notified or not self._queue:
                    return None
            return self._queue.pop(0)

    def put_unique(self, elem: Any) -> bool:
        """
        Puts an element in the queue only if not already present.
        :param elem: Element to be put in the queue.
        :return True: if the element was put in the queue, False otherwise.
        """
        with self._not_empty:
            if elem in self._queue:
                return False
            self._queue.append(elem)
            self._not_empty.notify()
            return True

    def put(self, elem: Any) -> None:
        """
        Adds a new item to the queue.
        :param elem: New item to be added.
        :return:
        """
        with self._not_empty:
            self._queue.append(elem)
            self._not_empty.notify()
