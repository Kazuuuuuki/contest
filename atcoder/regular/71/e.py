S = input()
T = input()
q = int(input())
A = [list(map(int, input().split())) for _ in range(q)]

count_s = [{"A": 0, "B":0} for i in range(len(S))]
count_t = [{"A": 0, "B":0} for i in range(len(T))]

for i in range(len(S)):
  if(S[i] == "A"):
    count_s[i]["A"] += 1
    if(i == len(S) -1):
      break
    count_s[i+1] = count_s[i].copy()
  else:
    count_s[i]["B"] += 1
    if(i == len(S) -1):
      break
    count_s[i+1] = count_s[i].copy()


for i in range(len(T)):
  if(T[i] == "A"):
    count_t[i]["A"] += 1
    if(i == len(T) -1):
      break
    count_t[i+1] = count_t[i].copy()
  else:
    count_t[i]["B"] += 1
    if(i == len(T) -1):
      break
    count_t[i+1] = count_t[i].copy()


for i in range(q):
  if(S[A[i][0] - 1] == "A"):
    count_S = {"A": count_s[A[i][1] - 1]["A"] - count_s[A[i][0] - 1]["A"] + 1, "B": count_s[A[i][1] - 1]["B"] - count_s[A[i][0] -1]["B"]}
  else:
    count_S = {"A": count_s[A[i][1] - 1]["A"] - count_s[A[i][0] - 1]["A"], "B": count_s[A[i][1] - 1]["B"] - count_s[A[i][0] -1]["B"] + 1}
  if(T[A[i][2] - 1] == "A"):
    count_T = {"A": count_t[A[i][3] - 1]["A"] - count_t[A[i][2] - 1]["A"] + 1, "B": count_t[A[i][3] - 1]["B"] - count_t[A[i][2] - 1]["B"]}
  else:
    count_T = {"A": count_t[A[i][3] - 1]["A"] - count_t[A[i][2] - 1]["A"], "B": count_t[A[i][3] - 1]["B"] - count_t[A[i][2] - 1]["B"] + 1}

  if(count_S["A"] - count_T["A"] > 0):
    tmp = count_S["A"] - count_T["A"] - (count_S["B"] - count_T["B"])
    if(tmp % 3 == 0):
      print("YES")
    else:
      print("NO")

  else:
    tmp = count_T["A"] - count_S["A"] - (count_T["B"] - count_S["B"])
    if(tmp % 3 == 0):
      print("YES")
    else:
      print("NO")