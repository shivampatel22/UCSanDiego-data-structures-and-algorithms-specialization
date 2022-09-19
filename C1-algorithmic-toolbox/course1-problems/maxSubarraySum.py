import sys

def maxSubarraySum(arr, N):
    minus_inf = -sys.maxsize - 1
    max_sum = minus_inf
    current_sum = 0
    poss_start = 0
    poss_end = 0
    curr_start = 0
    for i in range(N):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            poss_start = curr_start
            poss_end = i
        if current_sum < 0:
            current_sum = 0
            curr_start = i+1
    return (max_sum, poss_start, poss_end)

if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maxSubarraySum(arr, len(arr)))
