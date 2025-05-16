#!/usr/bin/env python3
import threading
import time
import random
from thread_safe_queue import ThreadSafeQueue

NUM_PRODUCERS = 50
NUM_CONSUMERS = 10
ITEMS_PER_PRODUCER = 1000
ITEMS_PER_CONSUMER = NUM_PRODUCERS * ITEMS_PER_PRODUCER / NUM_CONSUMERS

log_queue: ThreadSafeQueue = ThreadSafeQueue()

def producer(thread_id: int, queue: ThreadSafeQueue):
    for i in range(ITEMS_PER_PRODUCER):
        item = f"{thread_id}-{i}"
        success = queue.put_unique(item)
        if success:
            log_queue.put(f"[Producer {thread_id}] Added unique item: {item}")
        else:
            log_queue.put(f"[Producer {thread_id}] Duplicate item skipped: {item}")
        time.sleep(random.uniform(0.0001, 0.001))

def consumer(thread_id: int, queue: ThreadSafeQueue):
    popped = 0
    while popped < ITEMS_PER_CONSUMER:
        item = queue.pop()
        if item is None:
            log_queue.put(f"[Consumer {thread_id}] Timed out waiting for item.")
            continue
        popped += 1
        log_queue.put(f"[Consumer {thread_id}] Popped item: {item}")
        time.sleep(random.uniform(0.0001, 0.001))

def main():
    queue = ThreadSafeQueue()
    threads = [threading.Thread(target=producer, args=(i, queue)) for i in range(NUM_PRODUCERS)]
    threads.extend([threading.Thread(target=consumer, args=(i, queue)) for i in range(NUM_CONSUMERS)])
    [t.start() for t in threads]
    [t.join() for t in threads]
    for log in log_queue.get_queue():
        print(log)
    print(queue.size())

if __name__ == '__main__':
    main()
