#!/usr/bin/env python3
"""Module testing redis functionality"""
import redis
from typing import Union, Callable, Optional
from uuid import uuid4
from functools import wraps


def call_history(method: Callable) -> Callable:
    """decorator for storing inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """the actual wrapper"""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        input_ = str(args)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(input_key, input_)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """a function decorator for counting
        no of times class is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """the actual wrapper doint the job"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """class cache for redis"""
    def __init__(self):
        """stores redis instance and flushes"""
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """creates uuid4 key and stores the input data"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) \
            -> Union[str, bytes, float, int]:
        """ gets the val of a key value pair act on it according to fn"""
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return (val)

    def get_str(self, key: str) -> str:
        """ paramtrize Cache.get to str"""
        val = self._redis.get(key)
        return val.decode('utf-8')

    def get_int(self, key: str) -> int:
        """ parametrize .get to int"""
        val = self._redis.get(key)
        try:
            return int(val.decode('utf-8'))
        except Exception:
            val = 0
            return val
