S = input()

a = 0
b = 0
for i in range(len(S)):
  if(S[i] == "A"):
    a = i
    break

for i in range(len(S))[::-1]:
    if(S[i] == "Z"):
      b = i
      break

print(b - a + 1)