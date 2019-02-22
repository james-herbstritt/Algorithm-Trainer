from algtrainer import AlgSet, Timer
import random
import json
import time

class _Getch:
    """Gets a single character from standard input.
	Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = _Getch()

def main():
	with open("algsets/pll.json") as pll:
		algset = AlgSet.load_json(json.load(pll))

	t = Timer()

	try:
		while True:
			alg = random.choice(algset.algs)
			print(alg.name)
			time.sleep(1)
			print("\aStart")
			t.start()
			getch()
			t.stop()
			alg.times.append(t.elapsed())
			print(t.elapsed())
			c = getch()
			if c == "q":
				break
	except KeyboardInterrupt:
		pass
	print()
	print(json.dumps(algset.averages(), indent=4, sort_keys=True))

if __name__ == "__main__":
	main()
