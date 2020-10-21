import sys, unittest
from metrohash import metrohash64, metrohash128, MetroHash64, MetroHash128, bytes2hex

class TestMetrohash(unittest.TestCase):

	test_key_63 = b"012345678901234567890123456789012345678901234567890123456789012"

	def test_metrohash64(self):
		for cls, input, seed, truth in [
			(MetroHash64, self.test_key_63, 0, "6b753dae06704bad"),
			(MetroHash64, self.test_key_63, 1, "3b0d481cf4b9b8df"),
		]:
			h = cls(seed)
			h.update(input)

			self.assertEqual(truth, bytes2hex(h.digest()))
			self.assertEqual(truth, h.hexdigest())

	def test_metrohash64_update(self):
		for cls, input, seed, truth in [
			(MetroHash64, self.test_key_63, 0, "6b753dae06704bad"),
			(MetroHash64, self.test_key_63, 1, "3b0d481cf4b9b8df"),
		]:
			h = cls(seed)
			for i in range(0, len(input), 4):
				h.digest()
				h.update(input[i:i+4])

			self.assertEqual(truth, bytes2hex(h.digest()))
			self.assertEqual(truth, h.hexdigest())

	def test_metrohash64_copy(self):
		for cls, input, seed, truth in [
			(MetroHash64, self.test_key_63, 0, "6b753dae06704bad"),
			(MetroHash64, self.test_key_63, 1, "3b0d481cf4b9b8df"),
		]:
			h = cls(seed)
			for i in range(0, len(input), 4):
				h.update(input[i:i+4])
				h = h.copy()

			self.assertEqual(truth, bytes2hex(h.digest()))
			self.assertEqual(truth, h.hexdigest())

	def test_metrohash64_convenience(self):
		for func, input, seed, truth in [
			(metrohash64, self.test_key_63, 0, "6b753dae06704bad"),
			(metrohash64, self.test_key_63, 1, "3b0d481cf4b9b8df"),
		]:
			result = bytes2hex(func(input, seed))
			self.assertEqual(truth, result)

	def test_metrohash128(self):
		for cls, input, seed, truth in [
			(MetroHash128, self.test_key_63, 0, "c77ce2bfa4ed9f9b0548b2ac5074a297"),
			(MetroHash128, self.test_key_63, 1, "45a3cdb838199d7fbdd68d867a14ecef"),
		]:
			h = cls(seed)
			h.update(input)

			self.assertEqual(truth, bytes2hex(h.digest()))
			self.assertEqual(truth, h.hexdigest())

	def test_metrohash128_update(self):
		for cls, input, seed, truth in [
			(MetroHash128, self.test_key_63, 0, "c77ce2bfa4ed9f9b0548b2ac5074a297"),
			(MetroHash128, self.test_key_63, 1, "45a3cdb838199d7fbdd68d867a14ecef"),
		]:
			h = cls(seed)
			for i in range(0, len(input), 4):
				h.digest()
				h.update(input[i:i+4])

			self.assertEqual(truth, bytes2hex(h.digest()))
			self.assertEqual(truth, h.hexdigest())

	def test_metrohash128_copy(self):
		for cls, input, seed, truth in [
			(MetroHash128, self.test_key_63, 0, "c77ce2bfa4ed9f9b0548b2ac5074a297"),
			(MetroHash128, self.test_key_63, 1, "45a3cdb838199d7fbdd68d867a14ecef"),
		]:
			h = cls(seed)
			for i in range(0, len(input), 4):
				h.update(input[i:i+4])
				h = h.copy()

			self.assertEqual(truth, bytes2hex(h.digest()))
			self.assertEqual(truth, h.hexdigest())

	def test_metrohash128_convenience(self):
		for func, input, seed, truth in [
			(metrohash128, self.test_key_63, 0, "c77ce2bfa4ed9f9b0548b2ac5074a297"),
			(metrohash128, self.test_key_63, 1, "45a3cdb838199d7fbdd68d867a14ecef"),
		]:
			result = bytes2hex(func(input, seed))
			self.assertEqual(truth, result)

if __name__ == "__main__":
	unittest.main()
