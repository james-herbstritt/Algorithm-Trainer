import time

class Timer:
	def __init__(self):
		self.beginning = 0
		self.end = 0

	def start(self):
		self.beginning = time.perf_counter()

	def stop(self):
		self.end = time.perf_counter()

	def elapsed(self):
		return self.end - self.beginning
