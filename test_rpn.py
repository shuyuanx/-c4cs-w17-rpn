import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
	def test_exponentiation(self):
		newResult = rpn.calculate('2 3 ^')
		self.assertEqual(8, newResult)
		newResult = rpn.calculate('2 5 ^')
		self.assertEqual(32, newResult)
		newResult = rpn.calculate('3 2 ^')
		self.assertEqual(9, newResult)


if __name__ == "__main__":
	unittest.main(verbosity=2)