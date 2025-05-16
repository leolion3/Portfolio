# Python Thread-Safe Queue

This module implements a thread-safe queue using a list as the underlying data structure (`queue.Queue` was insufficient for the required use-case).

### Thread-safe operations:

- `put(elem: Any)`: Allows adding items to the queue.
- `put_unique(elem: Any) -> bool`: Allows adding items uniquely to the queue (no duplicates).
- `pop() -> Optional[Any]`: Pops the first element of the queue (FIFO) - blocking.
- `delete(elem: Any) -> bool`: Allows removing items from the queue.

### Unsafe (race conditions):

- `get_queue() -> List[Any]`: Gets a snapshot of the current queue.
- `contains(, elem: Any) -> bool`: Checks if a given element is present in the queue.
- `size() -> int`: Returns the current size of the queue.

### "Why would I use this over `queue.Queue`?"

This module was written to accommodate more fine-grained control over dynamic worker-threads and allow cancelling ongoing jobs. While the built-in `queue` is more than sufficient for most thread-safe operations, it just wasn't enough for the use case this module was written for.

Feel free to criticise multithreading problems and offer improvement suggestions.
