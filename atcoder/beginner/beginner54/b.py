n, m  = map(int, input().split())

a = []
b = []

for _ in range(n):
  a.append(list(input()))

for _ in range(m):
  b.append(list(input()))

for i in range(n-m+1):
  for j in range(n-m+1):
   flag = True
   for k in range(m):
     for l in range(m):
       if(a[i+k][j+l] != b[k][l]):
         flag = False
         break
     if(flag == False):
       break

   if(flag == True):
     print("Yes")
     exit()


print("No")