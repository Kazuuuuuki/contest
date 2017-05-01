A, B, C = map(int, input().split())

m = []
i = 0
while(True):
  i += 1
  r = (A*i) % B

  if(r in m):
    break
  m.append(r)

if(C in m):
  print("YES")
else:
  print("NO")