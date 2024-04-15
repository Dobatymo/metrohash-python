# distutils: language=c++

from cython.operator cimport dereference as deref
from libc.stdint cimport uint8_t, uint64_t


cdef extern from "metrohash.h" nogil:

	cdef cppclass CMetroHash64 "MetroHash64":
		CMetroHash64(const uint64_t seed)
		CMetroHash64(const CMetroHash64& copy)
		void Initialize(const uint64_t seed)
		void Update(const uint8_t* buffer, const uint64_t length)
		void Finalize(uint8_t* const result)
		@staticmethod
		void Hash(const uint8_t* buffer, const uint64_t length, uint8_t* const hash, const uint64_t seed)

	cdef cppclass CMetroHash128 "MetroHash128":
		CMetroHash128(const uint64_t seed)
		CMetroHash128(const CMetroHash128& copy)
		void Initialize(const uint64_t seed)
		void Update(const uint8_t* buffer, const uint64_t length)
		void Finalize(uint8_t* const result)
		@staticmethod
		void Hash(const uint8_t* buffer, const uint64_t length, uint8_t* const hash, const uint64_t seed)

__all__ = ["MetroHash128", "MetroHash64", "metrohash128", "metrohash64"]

cpdef bytes metrohash64(bytes data, uint64_t seed=0ULL):

	cdef bytearray out = bytearray(8)
	CMetroHash64.Hash(data, len(data), out, seed)
	return bytes(out)

cpdef bytes metrohash128(bytes data, uint64_t seed=0ULL):

	cdef bytearray out = bytearray(16)
	CMetroHash128.Hash(data, len(data), out, seed)
	return bytes(out)

cdef class MetroHash64(object):

	cdef CMetroHash64* _hasher

	@property
	def digest_size(self):
		return 8

	@property
	def block_size(self):
		return 32

	@property
	def name(self):
		return "metrohash64"

	def __cinit__(self, seed=0):
		cdef uint64_t _seed
		cdef MetroHash64 _copy
		if isinstance(seed, MetroHash64):
			_copy = <MetroHash64> seed
			self._hasher = new CMetroHash64(deref(_copy._hasher))
		else:
			_seed = <uint64_t> seed
			self._hasher = new CMetroHash64(_seed)

		if self._hasher is NULL:
			raise MemoryError()

	def __dealloc__(self):
		if self._hasher is not NULL:
			del self._hasher
			self._hasher = NULL

	def update(self, data):
		self._hasher.Update(data, len(data))

	cpdef digest(self):
		cdef bytearray _hash = bytearray(8)
		CMetroHash64(deref(self._hasher)).Finalize(_hash)
		return bytes(_hash)

	def hexdigest(self):
		return self.digest().hex()

	def copy(self):
		return MetroHash64(self)

cdef class MetroHash128(object):

	cdef CMetroHash128* _hasher

	@property
	def digest_size(self):
		return 16

	@property
	def block_size(self):
		return 64

	@property
	def name(self):
		return "metrohash128"

	def __cinit__(self, seed=0):
		cdef uint64_t _seed
		cdef MetroHash128 _copy
		if isinstance(seed, MetroHash128):
			_copy = <MetroHash128> seed
			self._hasher = new CMetroHash128(deref(_copy._hasher))
		else:
			_seed = <uint64_t> seed
			self._hasher = new CMetroHash128(_seed)

		if self._hasher is NULL:
			raise MemoryError()

	def __dealloc__(self):
		if self._hasher is not NULL:
			del self._hasher
			self._hasher = NULL

	def update(self, data):
		self._hasher.Update(data, len(data))

	cpdef digest(self):
		cdef bytearray _hash = bytearray(16)
		CMetroHash128(deref(self._hasher)).Finalize(_hash)
		return bytes(_hash)

	def hexdigest(self):
		return self.digest().hex()

	def copy(self):
		return MetroHash128(self)
