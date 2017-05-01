b = input().split()
a = [int(b[i]) for i in range(len(b))]

p = []

for j in range(a[0]):
  tmp = input().split()
  tmp = [int(tmp[i]) for i in range(2)]
  p.append((tmp[0], tmp[1]))

c = []

for j in range(a[1]):
  tmp = input().split()
  tmp = [int(tmp[i]) for i in range(2)]
  c.append((tmp[0], tmp[1]))

ans = []

for i in range(a[0]):
  min = (10000000000, 0)
  for j in range(a[1]):
    if(min[0] > abs(p[i][0] - c[j][0]) + abs(p[i][1] - c[j][1])):
      min = (abs(p[i][0] - c[j][0]) + abs(p[i][1] - c[j][1]), j+1)

  ans.append(min[1])

for j in range(a[0]):
  print(ans[j])

