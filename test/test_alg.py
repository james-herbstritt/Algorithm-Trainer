import unittest
from algtrainer import Algorithm

class TestCube(unittest.TestCase):
	def test_equality(self):
		alg = "R' U B2 L3 U2' U2"
		alg_rev = "U2 U2 L B2 U' R"
		self.assertEqual(Algorithm.reverse_alg(alg), alg_rev)

if __name__ == "__main__":
	unittest.main()
