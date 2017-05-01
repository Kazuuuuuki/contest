
def check1(a):
  sum = 0
  ans = 0
  for i in range(len(a)):
    if(i % 2 == 0):
      sum += a[i]
      if(sum >= 0):
        a[i] -= abs(sum)+1
        ans += abs(sum)+1
        sum -= abs(sum)+1
    else:
      sum += a[i]
      if(sum <= 0):
        a[i] += abs(sum)+1
        ans += abs(sum)+1
        sum += abs(sum)+1
  return ans

def check2(a):
  sum = 0
  ans = 0
  for i in range(len(a)):
    if(i % 2 == 0):
      sum += a[i]
      if(sum <= 0):
        a[i] += abs(sum)+1
        ans += abs(sum)+1
        sum += abs(sum)+1
    else:
      sum += a[i]
      if(sum >= 0):
        a[i] -= abs(sum)+1
        ans += abs(sum)+1
        sum -= abs(sum)+1
  return ans



n = input()
b = input().split()
a = [int(b[i]) for i in range(len(b))]
a2 = list(a)

ans1 = check1(a)
ans2 = check2(a2)


print(ans1) if(ans1<ans2) else print(ans2)