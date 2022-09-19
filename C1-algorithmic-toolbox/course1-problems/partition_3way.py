def partition3(a, l, r):
    x = a[l]
    m1 = l
    m2 = r
    i = l
    while (m1 <= m2):
        if a[i] < x:
            a[i], a[m1] = a[m1], a[i]
            i += 1
            m1 += 1
        elif a[i] > x:
            a[i], a[m2] = a[m2], a[i]
            m2 -= 1
        else:
            i += 1
            
    return m1, m2
        