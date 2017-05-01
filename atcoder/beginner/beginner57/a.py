b = input().split()
a = [int(b[i]) for i in range(len(b))]

if(a[0] + a[1] >= 24 ):
  print(a[0] + a[1] - 24)
else:
  print(a[0] + a[1])

  