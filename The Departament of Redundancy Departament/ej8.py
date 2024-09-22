from sys import stdin
from collections import Counter

nums = stdin.read().split()
conteo = Counter(nums)
for K in conteo:
    print(K,conteo[K])
