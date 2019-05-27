# distutils: language=c++

import sys
from libcpp cimport bool
from libc.stdint cimport uint64_t, uint8_t

"""
h = MetroHash128()
h.update('asd')
h.update('qwe')
h.digest()

is not the same as

h = MetroHash128()
h.update('asd')
h.digest()
h.update('qwe')
h.digest()

This is the same with hashlib.md5() for example
"""

cdef extern from "metrohash.h" nogil:

	cdef cppclass CMetroHash64 "MetroHash64":
		CMetroHash64(const uint64_t seed)
		void Initialize(const uint64_t seed)
		void Update(const uint8_t* buffer, const uint64_t length)
		void Finalize(uint8_t* const result)
		@staticmethod
		void Hash(const uint8_t* buffer, const uint64_t length, uint8_t* const hash, const uint64_t seed)

	cdef cppclass CMetroHash128 "MetroHash128":
		CMetroHash128(const uint64_t seed)
		void Initialize(const uint64_t seed)
		void Update(const uint8_t* buffer, const uint64_t length)
		void Finalize(uint8_t* const result)
		@staticmethod
		void Hash(const uint8_t* buffer, const uint64_t length, uint8_t* const hash, const uint64_t seed)

__all__ = ["MetroHash128", "MetroHash64", "metrohash128", "metrohash64"]

if sys.version_info < (3, ):
	def bytes2hex(b):
		return b.encode("hex")
else:
	def bytes2hex(b):
		return b.hex()

cpdef bytes metrohash64(bytes data, uint64_t seed=0ULL):

	cdef bytearray out = bytearray(b"\0"*8)
	CMetroHash64.Hash(data, len(data), out, seed)
	return bytes(out)

cpdef bytes metrohash128(bytes data, uint64_t seed=0ULL):

	cdef bytearray out = bytearray(b"\0"*16)
	CMetroHash128.Hash(data, len(data), out, seed)
	return bytes(out)

cdef class MetroHash64(object):

	cdef CMetroHash64* _hasher
	cdef bytearray _hash
	cdef bool _notfinal

	def __cinit__(self, uint64_t seed=0ULL):
		self._hasher = new CMetroHash64(seed)
		self._hash = bytearray(b"\0"*8)
		self._notfinal = True

		if self._hasher is NULL:
			raise MemoryError()

	def __dealloc__(self):
		if self._hasher is not NULL:
			del self._hasher
			self._hasher = NULL

	def update(self, data):
		if self._notfinal:
			self._hasher.Update(data, len(data))
		else:
			raise RuntimeError("Hash already finalized.")

	def digest(self):
		if self._notfinal:
			self._hasher.Finalize(self._hash)
			self._notfinal = False

		return bytes(self._hash)

	def hexdigest(self):
		return bytes2hex(self.digest())

cdef class MetroHash128(object):

	cdef CMetroHash128* _hasher
	cdef bytearray _hash
	cdef bool _notfinal

	def __cinit__(self, uint64_t seed=0ULL):
		self._hasher = new CMetroHash128(seed)
		self._hash = bytearray(b"\0"*16)
		self._notfinal = True

		if self._hasher is NULL:
			raise MemoryError()

	def __dealloc__(self):
		if self._hasher is not NULL:
			del self._hasher
			self._hasher = NULL

	def update(self, data):
		if self._notfinal:
			self._hasher.Update(data, len(data))
		else:
			raise RuntimeError("Hash already finalized.")

	def digest(self):
		if self._notfinal:
			self._hasher.Finalize(self._hash)
			self._notfinal = False

		return bytes(self._hash)

	def hexdigest(self):
		return bytes2hex(self.digest())
