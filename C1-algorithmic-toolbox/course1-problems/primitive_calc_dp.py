def dp_calculator(n):
    a_p = [None] * (n + 1)
    a_min_ops = [0] + [None] * n
    for i in range(1, n + 1):
        current_p = i - 1
        current_min_ops = a_min_ops[current_p] + 1
        if i % 3 == 0:
            p = i // 3
            num_ops = a_min_ops[p] + 1
            if num_ops < current_min_ops:
                current_p, current_min_ops = p, num_ops
        if i % 2 == 0:
            p = i // 2
            num_ops = a_min_ops[p] + 1
            if num_ops < current_min_ops:
                current_p, current_min_ops = p, num_ops

        a_p[i], a_min_ops[i] = current_p, current_min_ops
    nums = []
    i = n
    while i > 0:
        nums.append(i)
        i = a_p[i]
    nums.reverse()
    return nums, len(nums)
    
    
if __name__ == '__main__':
    n = int(input())
    num = [0] * n
    num, l = dp_calculator(n)
    print(l - 1)
    for i in range(l):
        print(num[i], end = ' ')
    


