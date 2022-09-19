def poly_multi_naive(p1, p2, n):
    product = [0] * (2*n - 1)
    for i in range(n):
        for j in range(n):
            product[i+j] += (p1[i] * p2[j])
    return product
    
if __name__ == '__main__':
    n = int(input())
    p1 = [int(p1) for p1 in input().split()]
    p2 = [int(p2) for p2 in input().split()]
    print(poly_multi_naive(p1, p2, n))