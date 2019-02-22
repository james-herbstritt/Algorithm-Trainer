from algtrainer import Cube

class Algorithm:

	def __init__(self, name, alg_str):
		self.name = name
		self.alg_str = alg_str
		self.cube = Algorithm.undo_alg(alg_str, "z2")
		self.times = []

	@staticmethod
	def reverse_alg(alg_str):
		moves = alg_str.split()
		for i, move in enumerate(moves):
			if len(move) == 1:
				moves[i] += "'"
			elif len(move) == 2 and move[1] in ("'", "3"):
				moves[i] = move[0]
			elif len(move) == 3 and move[1:3] == "2'":
				moves[i] = move[0:2]
		return " ".join(reversed(moves))

	@staticmethod
	def undo_alg(alg_str, premoves):
		rev_alg_str = Algorithm.reverse_alg(alg_str)
		p = " ".join((premoves, rev_alg_str))
		return Cube(premoves=p)

	@staticmethod
	def load_json(json):
		return Algorithm(json["name"], json["algorithm"])

	def dump_json(self):
		return {
			"name": self.name,
			"algorithm": self.alg_str,
			"times": self.times
		}
