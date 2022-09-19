"""One day Chinky was roaming around the park and suddenly she found N bags with diamonds.
The i'th of these bags contains Ai diamonds. She felt greedy and started to pick up the bag very fastly. But due to quick movement, she drops it on the ground.
But as soon as she drops the bag, a genie appears in front of her and he increases the number of diamonds in the bag suddenly!
Now the bag which was used to contain P diamonds(before picking up), now contains [P/2] diamonds, where [p] is the greatest integer less than p.
Then genie gave her the time K minutes in which she can take as many as diamonds. In a single minute , she can take all the diamonds in a single bag,
regardless the number of diamonds in it. Find the maximum number of diamonds that Chinky can take with her.
in: 5 3
    2 1 7 4 2
out: 14
"""


import heapq
def sol(arr, n, k):
    tot = 0
    h = []
    heapq.heapify(h)
    for elem in arr:
        heapq.heappush(h, -1*elem)
    for i in range(k):
        cur_max = -1*heapq.heappop(h)
        tot += cur_max
        heapq.heappush(h, -1*(cur_max//2))
        
    return tot

if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        arr = [int(x) for x in input().split()]
        print(sol(arr, n, k))
