from algtrainer import Algorithm

class AlgSet:
	def __init__(self, name, algs):
		self.name = name
		self.algs = algs

	@staticmethod
	def load_json(json):
		algs = [Algorithm.load_json(alg) for alg in json["algorithms"]]
		return AlgSet(json["set"], algs)

	def dump_json(self):
		algs = [alg.dump_json() for alg in self.algs]
		return { "set": self.name, "algorithms": algs }
