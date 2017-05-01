a = input()
b = input()

for i in range(len(a)):
  ans += a[i]
  if(i != len(a) - 1):
    ans += b[i]
  else:
    if(len(a) == len(b)):
      ans += b[i]

print(ans)
