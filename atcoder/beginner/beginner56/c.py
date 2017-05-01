import math

def gtime(X, a, t):
  l = math.floor((len(a)-1)/2)
  if(len(a) == 1):
    return a[0]
  if(a[l] <= X and t <= X - a[l] and a[l+1] + t + 1 > X):
    return a[l]

  elif(a[l] > X):
    return gtime(X, a[:l], t + 1)

  else:
    return gtime(X, a[l+1:], t + 1)





X = abs(int(input()))
a = [(i)*(i+1)/2 for i in range(X)]
ans = gtime(X, a, 1)
print(X - ans)

