

def change(s, i, n, ans):
  if(i == n-1):
    for j in range(-1, 2):
      if(j == 1 and s[0] == "o"):s[0] = "x"

      elif(j == 1 and s[0] != "o"): s[0] = "o"
      elif(s[i + j] == "o"): s[i + j] = "x"
      else: s[i + j] = "o"
  else:
    for j in range(-1, 2):
      if(s[i + j] == "o"): s[i + j] = "x"
      else: s[i + j] = "o"

  if(ans[i] == "S"):
    ans[i] = "W"
  else:
    ans[i] = "S"
  return (s, ans)

def check(a, s, ans, count, n):
  if(a == s):
    return ans
  if(count == 0):
    return -1
  tmp = [change(list(a), i, n, list(ans)) for i in range(n)]
  c = [check(list(tmp[i][0]), s, list(tmp[i][1]), count-1, n) for i in range(n)]
  while(-1 in c):
    c.remove(-1)
  if(len(c) >= 1):
    return c[0]
  else:
    return -1

N = int(input())
r = input()
s = [r[i] for i in range(N)]

a = ["o" for _ in range(N)]
ans = ["S" for _ in range(N)]

if(a == s):
  print(''.join(ans))
else:
  c = check(a, s, ans, N, N)
  if(c == -1):
    print(-1)
  else:
    print(''.join(c))
