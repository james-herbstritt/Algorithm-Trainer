# Michael Goodnow and James Herbstritt
from enum import Enum
from PIL import Image


class Color(Enum):
	white = 1
	yellow = 2
	red = 3
	orange = 4
	blue = 5
	green = 6


class Cube:
	# str -> Cube
	def __init__(self, rotate=""):

		# array of 9 colors
		self.U = [Color.white] * 9
		self.D = [Color.yellow] * 9
		self.R = [Color.red] * 9
		self.L = [Color.orange] * 9
		self.F = [Color.green] * 9
		self.B = [Color.blue] * 9

	@staticmethod
	def rotatedFace(orig_face, quarters):
		face = orig_face[:]
		for _ in range(quarters % 4):
			temp = face[0]
			face[0] = face[6]
			face[6] = face[8]
			face[8] = face[2]
			face[2] = temp
			temp = face[1]
			face[1] = face[3]
			face[3] = face[7]
			face[7] = face[5]
			face[5] = temp
		return face

	def doMoves(self, movesStr):
		for move in movesStr.split():
			self.doMove(move)

	# Cube str bool -> void
	def doMove(self, move):
		if len(move) == 2:
			move = move.replace("'", "3", 1)
			for i in range(int(move[1:2])):
				self.doMove(move[0:1])
		elif move == "U":
			self.U = Cube.rotatedFace(self.U, 1)
			temp = self.F[0:3]
			self.F[0:3] = self.R[0:3]
			self.R[0:3] = self.B[0:3]
			self.B[0:3] = self.L[0:3]
			self.L[0:3] = temp
		elif move == "D":
			self.D = Cube.rotatedFace(self.D, 1)
			temp = self.L[6:9]
			self.L[6:9] = self.B[6:9]
			self.B[6:9] = self.R[6:9]
			self.R[6:9] = self.F[6:9]
			self.F[6:9] = temp
		elif move == "R":
			self.R = Cube.rotatedFace(self.R, 1)
			temp = (self.B[i] for i in (6, 3, 0))
			self.B[6], self.B[3], self.B[0] = (self.U[i] for i in (2, 5, 8))
			self.U[2], self.U[5], self.U[8] = (self.F[i] for i in (2, 5, 8))
			self.F[2], self.F[5], self.F[8] = (self.D[i] for i in (2, 5, 8))
			self.D[2], self.D[5], self.D[8] = temp
		elif move == "L":
			self.L = Cube.rotatedFace(self.R, 1)
			temp = (self.D[i] for i in (0, 3, 6))
			self.D[0], self.D[3], self.D[6] = (self.F[i] for i in (0, 3, 6))
			self.F[2], self.F[5], self.F[8] = (self.U[i] for i in (0, 3, 6))
			self.U[6], self.U[3], self.U[0] = (self.B[i] for i in (8, 5, 2))
			self.B[8], self.B[5], self.B[2] = temp
		elif move == "F":
			self.F = Cube.rotatedFace(self.F, 1)
			temp = (self.U[i] for i in (6, 7, 8))
			self.U[6], self.U[7], self.U[8] = (self.L[i] for i in (8, 5, 2))
			self.L[8], self.L[5], self.L[2] = (self.D[i] for i in (2, 1, 0))
			self.D[2], self.D[1], self.D[0] = (self.R[i] for i in (0, 3, 6))
			self.R[0], self.R[3], self.R[6] = temp
		elif move == "B":
			self.F = Cube.rotatedFace(self.F, 1)
			temp = (self.U[i] for i in (2, 1, 0))
			self.U[2], self.U[1], self.U[0] = (self.R[i] for i in (8, 5, 2))
			self.R[8], self.R[5], self.R[2] = (self.D[i] for i in (6, 7, 8))
			self.D[6], self.D[7], self.D[8] = (self.L[i] for i in (0, 3, 6))
			self.L[0], self.L[3], self.L[6] = temp
		# Rotations
		elif move == "x":
			self.R = Cube.rotatedFace(self.R, 1)
			self.L = Cube.rotatedFace(self.L, 3)
			temp = Cube.rotatedFace(self.B, 2)
			self.B = Cube.rotatedFace(self.U, 2)
			self.U = self.F
			self.F = self.D
			self.D = temp
		elif move == "y":
			self.U = Cube.rotatedFace(self.U, 1)
			self.D = Cube.rotatedFace(self.D, 3)
			temp = self.F
			self.F = self.R
			self.R = self.B
			self.B = self.L
			self.L = temp
		elif move == "z":
			self.F = Cube.rotatedFace(self.F, 1)
			self.B = Cube.rotatedFace(self.B, 3)
			temp = self.U
			self.U = Cube.rotatedFace(self.L, 1)
			self.L = Cube.rotatedFace(self.D, 1)
			self.D = Cube.rotatedFace(self.R, 1)
			self.R = Cube.rotatedFace(temp, 1)
		# wide moves
		elif move == "u":
			self.doMove("D")
			self.doMove("y")
		elif move == "d":
			self.doMove("U")
			self.doMove("y'")
		elif move == "r":
			self.doMove("L")
			self.doMove("x")
		elif move == "l":
			self.doMove("R")
			self.doMove("x'")
		elif move == "f":
			self.doMove("B")
			self.doMove("z")
		elif move == "b":
			self.doMove("F")
			self.doMove("z'")
		# slice moves
		elif move == "M":
			self.doMove("x'")
			self.doMove("R")
			self.doMove("L'")
		elif move == "S":
			self.doMove("z")
			self.doMove("F'")
			self.doMove("B")
		elif move == "E":
			self.doMove("y")
			self.doMove("U'")
			self.doMove("D")
		else:
			print("Invalid move.")
	
	# Cube str -> "image"
	def drawFace(self, face):
		print("Not Implemented")