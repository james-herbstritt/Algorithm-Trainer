from algtrainer import AlgSet, Timer
import random
import json
import time

def main():
	with open("algsets/pll.json") as pll:
		algset = AlgSet.load_json(json.load(pll))

	t = Timer()

	try:
		while True:
			alg = random.choice(algset.algs)
			print(alg.name)
			time.sleep(1)
			t.start()
			input("Start")
			t.stop()
			alg.times.append(t.elapsed())
			print(t.elapsed())
	except KeyboardInterrupt:
		pass
	print()
	print(json.dumps(algset.dump_json(), indent=4, sort_keys=True))



if __name__ == "__main__":
	main()
