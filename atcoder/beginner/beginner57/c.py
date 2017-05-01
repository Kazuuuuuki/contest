import math

a = int(input())

def prime(i):
  for j in range(int(math.sqrt(i))+ 1):
    j += 2
    if(i % j == 0):
      return j

  return i

b = prime(a)

array = {}
category = []
while(True):

  if(not b in array):
    array[b] = 1
    category.append(b)
  else:
    array[b] += 1

  a = int(a / b)
  b = prime(a)
  if(b == a):
    if(not b in array):
      array[b] = 1
      category.append(b)
    else:
      array[b] += 1
    break

ans = (1, 1)


for i in reversed(category):
  for _ in range(array[i]):
    if(ans[0] > ans[1]):
      ans =  (ans[0], ans[1]*i)
    else:
      ans =  (ans[0]*i, ans[1])

if(ans[0] > ans[1]):
  print(len(str(ans[0])))
else:
  print(len(str(ans[1])))



