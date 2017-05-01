
N, D = list(map(int,input().split()))
d = list(map(int,input().split()))
Q = int(input())
q = list(map(int,input().split()))

a = [D for _ in range(N)]
b = [1 for _ in range(N+1)]

for i in range(1, N):
  a[i] = min(abs(a[i-1] - d[i-1]), a[i-1])

for i in range(N)[::-1]:
    if d[i] // 2 < b[i+1]:
       b[i] = b[i+1] + d[i]
     