W, a, b = map(int, input().split())

abs = max(a, b) - min(a, b) - W

print(max(0, abs))