from itertools import combinations_with_replacement
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
for i in sorted(set(combinations_with_replacement(arr, M))):
    print(*i)
