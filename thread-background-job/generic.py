import threading
from functools import wraps
from typing import Self
from contextlib import contextmanager


class BackgroundJobManager:
    _instance = None
    _lock = threading.Lock()
    _threads = []

    def __new__(cls, *args, **kwargs) -> Self:
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls, *args, **kwargs)
                    cls._instance._threads = []
        return cls._instance
    
    def job(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=func, args=args, kwargs=kwargs)
            self._threads.append(thread)
            thread.start()
            return thread
        return wrapper
    
    @contextmanager
    def wait(self):
        try:
            yield
        finally:
            for thread in self._threads:
                thread.join()
