"""print the nodes without siblings"""
import sys, collections
class tree():
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def withoutSiblings(self):
        self.result = []
        node = 0
        dq = collections.deque([node])
        while len(dq) != 0:
            N = dq.popleft()
            if self.left[N] != -1:
                dq.append(self.left[N])
                if self.right[N] == -1:
                    self.result.append(self.key[self.left[N]])
            if self.right[N] != -1:
                dq.append(self.right[N])
                if self.left[N] == -1:
                    self.result.append(self.key[self.right[N]])
        return self.result

if __name__ == '__main__':
    t = tree()
    t.read()
    print(t.withoutSiblings())
        
