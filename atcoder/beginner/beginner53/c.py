x = int(input())
q = x // 11
m = x % 11
if(m == 0):
  print(q * 2)
elif(m < 7):
  print(q * 2 + 1)
else:
  print(q * 2 + 2)