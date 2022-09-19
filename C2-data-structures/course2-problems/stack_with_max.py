#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__auxStack = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__auxStack) == 0:
            self.__auxStack.append(a)
        else:
            if a > self.__auxStack[-1]:
                self.__auxStack.append(a)
            else:
                self.__auxStack.append(self.__auxStack[-1])

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__auxStack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__auxStack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
