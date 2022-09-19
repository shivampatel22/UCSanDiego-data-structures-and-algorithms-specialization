def isGreaterOrEqual(maxDigit, num):
    """As the last question of a successful interview, your boss gives you a few pieces 
    of paper with numbers on it and asks you to compose a largest number from these numbers.
    The resulting number is going to be your salary, so you are very much interested in
    maximizing this number. How can you do this? """
    num1 = str(maxDigit) + str(num)
    num2 = str(num) + str(maxDigit)
    if int(num2) > int(num1):
        return True
    else:
        return False

def maxNum(nums):
    res = []
    while len(nums) != 0:
        maxDigit = 0
        for num in nums:
            if isGreaterOrEqual(maxDigit, num):
                maxDigit = num
        res.append(str(maxDigit))
        nums.remove(maxDigit)
    print("".join(res))

n = int(input())
nums = [int(nums) for nums in input().split()]
maxNum(nums)
        