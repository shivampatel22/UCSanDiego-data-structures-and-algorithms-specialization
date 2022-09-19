import sys

class Solve:
	def __init__(self, s):
		self.s = s
	def enquire(self, a, b, l):
		return s[a:a+l] == s[b:b+l]

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solve(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.enquire(a, b, l) else "No")