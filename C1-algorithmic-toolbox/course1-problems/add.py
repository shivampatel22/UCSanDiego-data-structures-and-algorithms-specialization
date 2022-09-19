def add(a, b):
    c = a + b
    return c
    
if __name__ == '__main__':
    a, b = map(int, input().split())
    print(add(a, b))