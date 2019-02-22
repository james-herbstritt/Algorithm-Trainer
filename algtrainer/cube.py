# Michael Goodnow and James Herbstritt
from enum import Enum
from PIL import Image, ImageDraw


class Color(Enum):
	white = 1
	yellow = 2
	red = 3
	orange = 4
	blue = 5
	green = 6


class Cube:
	# str -> Cube
	def __init__(self, premoves=""):

		# array of 9 colors
		self.U = [Color.white] * 9
		self.D = [Color.yellow] * 9
		self.R = [Color.red] * 9
		self.L = [Color.orange] * 9
		self.F = [Color.green] * 9
		self.B = [Color.blue] * 9

		self.do_moves(premoves)

	def __eq__(self, other):
		if not isinstance(other, Cube):
			return False
		sameU = self.U == other.U
		sameD = self.D == other.D
		sameR = self.R == other.R
		sameL = self.L == other.L
		sameF = self.F == other.F
		sameB = self.B == other.B
		sameCube = sameU and sameD and sameR and sameL and sameF and sameB
		return sameCube

	@staticmethod
	def rotated_face(orig_face, quarters):
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

	def do_moves(self, moves_str):
		for move in moves_str.split():
			self.do_move(move)

	# Cube str bool -> void
	def do_move(self, move):
		if len(move) == 2:
			normalized = move.replace("'", "3", 1)
			try:
				for _ in range(int(normalized[1:2])):
					self.do_move(normalized[0:1])
			except ValueError:
				raise ValueError("Invalid move: %s." % move)
		elif move == "U":
			self.U = Cube.rotated_face(self.U, 1)
			temp = self.F[0:3]
			self.F[0:3] = self.R[0:3]
			self.R[0:3] = self.B[0:3]
			self.B[0:3] = self.L[0:3]
			self.L[0:3] = temp
		elif move == "D":
			self.D = Cube.rotated_face(self.D, 1)
			temp = self.L[6:9]
			self.L[6:9] = self.B[6:9]
			self.B[6:9] = self.R[6:9]
			self.R[6:9] = self.F[6:9]
			self.F[6:9] = temp
		elif move == "R":
			self.R = Cube.rotated_face(self.R, 1)
			temp = tuple(self.B[i] for i in (6, 3, 0))
			self.B[6], self.B[3], self.B[0] = tuple(
				self.U[i] for i in (2, 5, 8))
			self.U[2], self.U[5], self.U[8] = tuple(
				self.F[i] for i in (2, 5, 8))
			self.F[2], self.F[5], self.F[8] = tuple(
				self.D[i] for i in (2, 5, 8))
			self.D[2], self.D[5], self.D[8] = temp
		elif move == "L":
			self.L = Cube.rotated_face(self.L, 1)
			temp = tuple(self.D[i] for i in (0, 3, 6))
			self.D[0], self.D[3], self.D[6] = tuple(
				self.F[i] for i in (0, 3, 6))
			self.F[0], self.F[3], self.F[6] = tuple(
				self.U[i] for i in (0, 3, 6))
			self.U[0], self.U[3], self.U[6] = tuple(
				self.B[i] for i in (8, 5, 2))
			self.B[8], self.B[5], self.B[2] = temp
		elif move == "F":
			self.F = Cube.rotated_face(self.F, 1)
			temp = tuple(self.U[i] for i in (6, 7, 8))
			self.U[6], self.U[7], self.U[8] = tuple(
				self.L[i] for i in (8, 5, 2))
			self.L[8], self.L[5], self.L[2] = tuple(
				self.D[i] for i in (2, 1, 0))
			self.D[2], self.D[1], self.D[0] = tuple(
				self.R[i] for i in (0, 3, 6))
			self.R[0], self.R[3], self.R[6] = temp
		elif move == "B":
			self.B = Cube.rotated_face(self.B, 1)
			temp = tuple(self.U[i] for i in (2, 1, 0))
			self.U[2], self.U[1], self.U[0] = tuple(
				self.R[i] for i in (8, 5, 2))
			self.R[8], self.R[5], self.R[2] = tuple(
				self.D[i] for i in (6, 7, 8))
			self.D[6], self.D[7], self.D[8] = tuple(
				self.L[i] for i in (0, 3, 6))
			self.L[0], self.L[3], self.L[6] = temp
		# Rotations
		elif move == "x":
			self.R = Cube.rotated_face(self.R, 1)
			self.L = Cube.rotated_face(self.L, 3)
			temp = Cube.rotated_face(self.B, 2)
			self.B = Cube.rotated_face(self.U, 2)
			self.U = self.F
			self.F = self.D
			self.D = temp
		elif move == "y":
			self.U = Cube.rotated_face(self.U, 1)
			self.D = Cube.rotated_face(self.D, 3)
			temp = self.F
			self.F = self.R
			self.R = self.B
			self.B = self.L
			self.L = temp
		elif move == "z":
			self.F = Cube.rotated_face(self.F, 1)
			self.B = Cube.rotated_face(self.B, 3)
			temp = self.U
			self.U = Cube.rotated_face(self.L, 1)
			self.L = Cube.rotated_face(self.D, 1)
			self.D = Cube.rotated_face(self.R, 1)
			self.R = Cube.rotated_face(temp, 1)
		# wide moves
		elif move == "u":
			self.do_move("D")
			self.do_move("y")
		elif move == "d":
			self.do_move("U")
			self.do_move("y'")
		elif move == "r":
			self.do_move("L")
			self.do_move("x")
		elif move == "l":
			self.do_move("R")
			self.do_move("x'")
		elif move == "f":
			self.do_move("B")
			self.do_move("z")
		elif move == "b":
			self.do_move("F")
			self.do_move("z'")
		# slice moves
		elif move == "M":
			self.do_move("x'")
			self.do_move("R")
			self.do_move("L'")
		elif move == "S":
			self.do_move("z")
			self.do_move("F'")
			self.do_move("B")
		elif move == "E":
			self.do_move("y")
			self.do_move("U'")
			self.do_move("D")
		else:
			raise ValueError("Invalid move: %s." % move)

	# Cube str -> "image"
	def draw_u_face(self, face):

		img = Image.new('RGBA', (400, 400), (255, 255, 255, 0))

		draw = ImageDraw.Draw(img)

		for j in range(3):
			for i in range(3):
				color = self.U[j * 3 + i].name
				print(i, j)
				x0, x1 = (100 * i + 50, 100 * (i + 1) - 1 + 50)
				y0, y1 = (100 * j + 50, 100 * (j + 1) - 1 + 50)
				print(x0, y0, x1, y1)
				draw.rectangle([x0, y0, x1, y1], fill=color, outline="black")

		# draw F
		x0, y0 = (50, 350)
		for x in range(3):
			color = self.F[x].name
			x1, y1 = (x0 + 100 - 1, y0 + 50 - 1)
			draw.rectangle([x0, y0, x1, y1], fill=color, outline="black")
			x0 += 100

		# draw R
		x0, y0 = (350, 50)
		for x in range(3):
			color = self.R[2 - x].name
			x1, y1 = (x0 + 50 - 1, y0 + 100 - 1)
			draw.rectangle([x0, y0, x1, y1], fill=color, outline="black")
			y0 += 100

		# draw B
		x0, y0 = (50, 0)
		for x in range(3):
			color = self.B[2 - x].name
			x1, y1 = (x0 + 100 - 1, y0 + 50 - 1)
			draw.rectangle([x0, y0, x1, y1], fill=color, outline="black")
			x0 += 100

		# draw L
		x0, y0 = (0, 50)
		for x in range(3):
			color = self.L[x].name
			x1, y1 = (x0 + 50 - 1, y0 + 100 - 1)
			draw.rectangle([x0, y0, x1, y1], fill = color, outline="black")
			y0 += 100
		return img
