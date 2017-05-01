import sys

sys.setrecursionlimit(10000)


def memoize(f):
    cache = {}

    def func(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return func


@memoize



def combi(n, r):
  if r == 0 or n == r:
    return 1
  return combi(n-1, r-1) + combi(n-1, r)

n, a, b = map(int, input().split())
items = sorted(map(int, input().split()), reverse=True)
max_ave_list = items[:a]
print(sum(max_ave_list)/len(max_ave_list))

m = max_ave_list.count(max_ave_list[-1])
l = items.count(max_ave_list[-1])
if l == m:
  print(1)
elif max_ave_list[0] != max_ave_list[-1]:
  print(combi(l, m))
else:
  print(sum(combi(l, k) for k in range(m, min(b, l) + 1)))