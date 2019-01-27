# Michael Goodnow, James Herbstritt

import unittest
from algtrainer import Cube

class TestCube(unittest.TestCase):
	def test_equality(self):
		self.assertEqual(Cube(), Cube())

	def test_do_move(self):
		cube1 = Cube()
		cube = Cube()
		cube.do_move("F")
		cube.do_move("F'")
		self.assertEqual(cube, cube1)
		for _ in range(6):
			cube.do_move("R")
			cube.do_move("U")
			cube.do_move("R'")
			cube.do_move("U'")
		self.assertEqual(cube, cube1)

	def test_do_moves(self):
		cube1 = Cube()
		cube2 = Cube()
		cube1.do_move("F")
		cube1.do_move("R")
		cube1.do_move("U")
		cube1.do_move("R'")
		cube1.do_move("U'")
		cube1.do_move("F'")
		cube2.do_moves("F R U R' U' F'")
		self.assertEqual(cube1, cube2)


if __name__ == "__main__":
	unittest.main()
