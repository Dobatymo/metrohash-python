# metrohash-python

Python bindings for the fast non-cryptograpical hash function MetroHash. MetroHash C++ library by J. Andrew Rogers, Python bindings by Dobatymo.

## Requirements

The library has been tested on Linux Python 2.7 and 3.6, and on Windows Python 3.5, 3.6, 3.7.

## Install

```
pip install metrohash-python
```

Compilation requires a C++ compiler and optionally `Cython`.

## Examples

The usage is similar to Python's hashlib.

```python
>>> import metrohash
>>> h = metrohash.MetroHash128()
>>> h.update(b'asd')
>>> h.update(b'qwe')
>>> h.digest()
b'K\xfb\x17\xeb>\xb2W\xbd\x93\xad\xf6\x17\xceg\x14\xda'
>>> h.hexdigest()
'4bfb17eb3eb257bd93adf617ce6714da'
```

Or as simple non-incremental function:

```python
>>> import metrohash
>>> metrohash.metrohash128(b'asdqwe')
b'K\xfb\x17\xeb>\xb2W\xbd\x93\xad\xf6\x17\xceg\x14\xda'
```

The interface for `MetroHash64` and `metrohash64` is the same.
