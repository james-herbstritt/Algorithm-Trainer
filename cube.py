# Michael Goodnow and James Herbstritt
from enum import Enum

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
		U = [Color.white] * 9 
		D = [Color.yellow] * 9
		R = [Color.red] * 9 
		L = [Color.orange] * 9
		B = [Color.blue] * 9
		F = [Color.green] * 9
	
	
	# Cube str bool -> void
	def doMove(self, moveStr, backwards=False):
		moves = moveStr.split()
		for move in moves:
			if move == "U":
				
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
			else: 
				print ("BAD BAD BAD")

		print("Not Implemented")
	
	# Cube str -> "image"
	drawFace(self, face):
		print("Not Implemented")
