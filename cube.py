# Michael Goodnow and James Herbstritt
from enum import Enum

class Color(Enum):
	white = 1
	yellow = 2
	red = 3
	orange = 4
	blue = 5
	green = 6

class Face(Enum):
	U = 0
	D = 1
	R = 2
	L = 3
	F = 4
	B = 5
	
	
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
		quarters %= 4;
		face = orig_face[:]
		for _ in range(quarters):
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
			
		
	
	# Cube str bool -> void
	def doMove(self, moveStr):
		moves = moveStr.split()
		for move in moves:
			if move == "U":
				rotateFace(self.U, 1)
				temp = self.F[0:3]
				self.F[0:3] = self.R[0:3]
				self.R[0:3] = self.B[0:3]
			elif move == "U'":
				
			elif move == "U2":
				do stuff 
			elif move == "D":
				do stuff 
			elif move == "D'":
				do stuff 
			elif move == "D2":
				do stuff 
			elif move == "R":
				do stuff 
			elif move == "R''":
				do stuff 
			elif move == "R2":
				do stuff 
			elif move == "L":
				do stuff 
			elif move == "L'":
				do stuff 
			elif move == "L2":
				do stuff 
			elif move == "B":
				do stuff 
			elif move == "B'":
				do stuff 
			elif move == "B2":
				do stuff 
			elif move == "F":
				do stuff 
			elif move == "F'":
				do stuff 
			elif move == "F2":
				do stuff
			# Rotations
			elif move == "x":
				do stuff 
			elif move == "x'":
				do stuff 
			elif move == "x2":
				do stuff 
			elif move == "y":
				do stuff 
			elif move == "y'":
				do stuff 
			elif move == "y2":
				do stuff 
			elif move == "z":
				do stuff 
			elif move == "z'":
				do stuff 
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
