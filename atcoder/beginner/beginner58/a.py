b = input().split()
a = [int(b[i]) for i in range(len(b))]

print("YES") if (a[1] - a[0] == a[2] - a[1]) else print("NO")