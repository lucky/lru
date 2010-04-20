=======================================
A simple LRU (Last-recently-used) cache
=======================================

You can install from pypi using pip or easy_install::

    easy_install lru

Usage::

    >>> from lru import LRUCache
    >>> cache = LRUCache(max_items=2)
    >>> cache['foo'] = 1
    >>> cache['bar'] = 10
    >>> cache['baz'] = 100 # `foo` is removed
    >>> cache['bar']
    10
    >>> cache['foo']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/Library/Python/2.6/site-packages/lru.py", line 18, in __getitem__
        raise KeyError, key
    KeyError: 'foo'


A `KeyError` is raised if the key is requested but does not exist, just like a
dictionary.
