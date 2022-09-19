def fiboSquareSum(n):
    """ Compute the last digit of F0^2 + F1^2 +···+ Fn^2 . """
    period_length = 60
    period = "011235831459437077415617853819099875279651673033695493257291"
    r = n % period_length
    for i in range(r+1):
        ld1 = int(period[i])
    ld2 = int(period[(i+1)%period_length])
    return (ld1 * ld2)%10

if __name__ == '__main__':
    n = int(input())
    print(fiboSquareSum(n))