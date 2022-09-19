def LastDigitFiboSum(n):
    """ Given an integer n, find the last digit of the sum F0 + F1 +···+ Fn. """
    period_length = 60
    period = "011235831459437077415617853819099875279651673033695493257291"
    period_sum = 0
    total_sum = 0
    for num in period:
        period_sum = (period_sum + int(num))%10
    q = n // period_length
    r = n % period_length
    for i in range(r+1):
        total_sum = (total_sum + int(period[i]))%10
    total_sum = (total_sum + (q*period_sum))%10
    return total_sum
    
if __name__ == '__main__':
    n = int(input())
    print(LastDigitFiboSum(n))
        
        