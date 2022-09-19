def LastDigitFiboSum(a):
    """ Given two non-negative integers m and n, where m ≤ n, find the last 
    digit of the sum Fm + Fm+1 + ···+ Fn. """
    period_length = 60
    period = "011235831459437077415617853819099875279651673033695493257291"
    period_sum = 0
    total_sum = 0
    for num in period:
        period_sum = (period_sum + int(num))%10
    q = a // period_length
    r = a % period_length
    for i in range(r+1):
        total_sum = (total_sum + int(period[i]))%10
    total_sum = (total_sum + (q*period_sum))%10
    return total_sum
    
if __name__ == '__main__':
    m, n = map(int, input().split())
    n_sum = LastDigitFiboSum(n)
    m_sum = LastDigitFiboSum(m-1)
    if n_sum >= m_sum:
        print(n_sum - m_sum)
    else:
        print(n_sum+10 - m_sum)