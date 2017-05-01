#
# N, W = map(int, input().split())
# w = []
# v = []
#
# for _ in range(N):
#   tmp = input().split()
#   w.append(int(tmp[0]))
#   v.append(int(tmp[1]))
#
# dp = []
#
# for i in range(W+1):
#   dp.append([])
#   dp[i] = [0] * (N + 1)
#   for j in range(N+1):
#     if(j == 0):
#       continue
#     if(i - w[j-1] >= 0):
#       dp[i][j] = max(dp[i][j-1], dp[i-w[j-1]][j-1] + v[j-1], dp[i][j])
#     else:
#       dp[i][j] = max(dp[i][j-1], dp[i][j])
# print(dp[W][N])
#


N, W = map(int, input().split())
w, v = [0] * N, [0] * N

for i in range(N):
  w[i], v[i] = map(int, input().split())

memo = {i:{} for i in range(N)}

def r(i, g):
  global memo
  if i == N:
      return 0
  elif g in memo[i]:
      return memo[i][g]
  elif g < w[i]:
      a = r(i + 1, g)
  else:
      a = max(r(i + 1, g - w[i]) + v[i], r(i + 1, g))

  memo[i][g] = a
  return a

print(r(0, W))