b = input().split()
c = [int(b[i]) for i in range(len(b))]

d = input().split()
e = [int(d[i]) for i in range(c[0])]

r = input().split()
f = [int(r[i]) for i in range(c[1])]

ansx = 0
for i in range(c[0]):
  tmp = i*e[i] - (c[0]-i-1)*e[i]
  ansx += tmp

ansy = 0
for j in range(c[1]):
  tmp = j*f[j] - (c[1]-j-1)*f[j]
  ansy += tmp

print((ansx * ansy) % (10**9 + 7))