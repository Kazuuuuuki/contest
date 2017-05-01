N = int(input())
A = list(map(int, input().split()))

C = {}

for i in range(N):
  if not A[i] in C:
    C[A[i]] = 1
  else:
    C[A[i]] += 1

ans = 0
count = 0
for key, value in C.items():
  ans += 1
  if(value % 2 == 0):
    count += 1

if(count % 2 == 0):
  print(ans)
else:
  print(ans-1)
