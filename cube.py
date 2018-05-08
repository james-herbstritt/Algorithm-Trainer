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
	def __init__(self, rotate = ""):

		# array of 9 colors
		self.U = [Color.white] * 9 
		self.D = [Color.yellow] * 9
		self.R = [Color.red] * 9 
		self.L = [Color.orange] * 9
		self.F = [Color.green] * 9
		self.B = [Color.blue] * 9
	
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
			
	# Cube str bool -> void
	def doMove(self, moveStr):
		moves = moveStr.split()
		for move in moves:
			if move == "U":
				self.U = rotatedFace(self.U, 1)
				temp = self.F[0:3]
				self.F[0:3] = self.R[0:3]
				self.R[0:3] = self.B[0:3]
				self.B[0:3] = self.L[0:3]
				self.L[0:3] = temp
			elif move == "U'":
				doMove(self, "U")
				doMove(self, "U")
				doMove(self, "U")
			elif move == "U2":
				doMove(self, "U")
				doMove(self, "U")
			elif move == "D":
				self.D = rotatedFace(self.D, 1)
				temp = self.L[6:9]
				self.L[6:9] = self.B[6:9]
				self.B[6:9] = self.R[6:9]
				self.R[6:9] = self.F[6:9]
				self.F[6:9] = temp
			elif move == "D'":
				doMove(self, "D")
				doMove(self, "D")
				doMove(self, "D")
			elif move == "D2":
				doMove(self, "D")
				doMove(self, "D")
			elif move == "R":
				self.R = rotatedFace(self.R, 1)
				temp = (self.B[i] for i in (6, 3, 0))
				self.B[6], self.B[3], self.B[0] = (self.U[i] for i in (2, 5, 8))
				self.U[2], self.U[5], self.U[8] = (self.F[i] for i in (2, 5, 8))
				self.F[2], self.F[5], self.F[8] = (self.D[i] for i in (2, 5, 8))
				self.D[2], self.D[5], self.D[8] = temp
			elif move == "R'":
				doMove(self, "R")
				doMove(self, "R")
				doMove(self, "R")
			elif move == "R2":
				doMove(self, "R")
				doMove(self, "R")
			elif move == "L":
				self.L = rotatedFace(self.R, 1)
				temp = (self.D[i] for i in (0, 3, 6))
				self.D[0], self.D[3], self.D[6] = (self.F[i] for i in (0, 3, 6))
				self.F[2], self.F[5], self.F[8] = (self.U[i] for i in (0, 3, 6))
				self.U[6], self.U[3], self.U[0] = (self.B[i] for i in (8, 5, 2))
				self.B[8], self.B[5], self.B[2] = temp
			elif move == "L'":
				doMove(self, "L")
				doMove(self, "L")
				doMove(self, "L")
			elif move == "L2":
				doMove(self, "L")
				doMove(self, "L")
			elif move == "F":
				self.F = rotatedFace(self.F, 1)
				temp = (self.U[i] for i in (6, 7, 8))
				self.U[6], self.U[7], self.U[8] = (self.L[i] for i in (8, 5, 2))
				self.L[8], self.L[5], self.L[2] = (self.D[i] for i in (2, 1, 0))
				self.D[2], self.D[1], self.D[0] = (self.R[i] for i in (0, 3, 6))
				self.R[0], self.R[3], self.R[6] = temp
			elif move == "F'":
				doMove(self, "F")
				doMove(self, "F")
				doMove(self, "F")
			elif move == "F2":
				doMove(self, "F")
				doMove(self, "F")
			elif move == "B":
				self.F = rotatedFace(self.F, 1)
				temp = (self.U[i] for i in (2, 1, 0))
				self.U[2], self.U[1], self.U[0] = (self.R[i] for i in (8, 5, 2))
				self.R[8], self.R[5], self.R[2] = (self.D[i] for i in (6, 7, 8))
				self.D[6], self.D[7], self.D[8] = (self.L[i] for i in (0, 3, 6))
				self.L[0], self.L[3], self.L[6] = temp
			elif move == "B'":
				doMove(self, "B")
				doMove(self, "B")
				doMove(self, "B")
			elif move == "B2":
				doMove(self, "B")
				doMove(self, "B")
			# Rotations
			elif move == "x":
				self.R = rotatedFace(self.R, 1)
				self.L = rotatedFace(self.L, 3)
				temp = rotatedFace(self.B, 2)
				self.B = rotatedFace(self.U, 2)
				self.U = self.F
				self.F = self.D
				self.D = temp
			elif move == "x'":
				doMove(self, "x")
				doMove(self, "x")
				doMove(self, "x")
			elif move == "x2":
				doMove(self, "x")
				doMove(self, "x")
			elif move == "y":
				self.U = rotatedFace(self.U, 1)
				self.D = rotatedFace(self.D, 3)
				temp = self.F
				self.F = self.R
				self.R = self.B
				self.B = self.L
				self.L = temp 
			elif move == "y'":
				doMove(self, "y")
				doMove(self, "y")
				doMove(self, "y")
			elif move == "y2":
				doMove(self, "y")
				doMove(self, "y")
			elif move == "z":
				self.F = rotatedFace(self.F, 1)
				self.B = rotatedFace(self.B, 3)
				temp = self.U
				self.U = rotatedFace(self.L, 1)
				self.L = rotatedFace(self.D, 1)
				self.D = rotatedFace(self.R, 1)
				self.R = rotatedFace(temp, 1)
			elif move == "z'":
				do stuff ,
			elif move == "z2":
				do stuff
			# wide moves
			elif move == "u":
				do stuff 
			elif move == "u'":
				do stuff 
			elif move == "u2":
				do stuff 
			elif move == "d":
				do stuff 
			elif move == "d'":
				do stuff 
			elif move == "d2":
				do stuff 
			elif move == "r":
				do stuff 
			elif move == "r'":
				do stuff 
			elif move == "r2":
				do stuff 
			elif move == "l":
				do stuff 
			elif move == "l'":
				do stuff 
			elif move == "l2":
				do stuff 
			elif move == "b":
				do stuff 
			elif move == "b'":
				do stuff 
			elif move == "b2":
				do stuff 
			elif move == "f":
				do stuff 
			elif move == "f'":
				do stuff 
			elif move == "f2":
				do stuff
			# slice moves 
			elif move == "M":
				do stuff 
			elif move == "M'":
				do stuff 
			elif move == "M2":
				do stuff 
			elif move == "S":
				do stuff 
			elif move == "S'":
				do stuff 
			elif move == "S2":
				do stuff 
			elif move == "E":
				do stuff 
			elif move == "E'":
				do stuff 
			elif move == "E2":
				do stuff 
			else: 
				print ("BAD BAD BAD")

		print("Not Implemented")
	
	# Cube str -> "image"
	drawFace(self, face):
		print("Not Implemented")



if __name__ == __main__:
	