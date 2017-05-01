N, K = map(int, input().split())
a = [int(i) for i in input().split()]
ans = 0
for k in range(N):
    tmp = a[k]
    a[k] = 0
    dp = []
    for i in range(N):
      dp.append([])
      for j in range(K+1):
        if(j == 0):
          dp[i].append(True)
          continue
        dp[i].append(False)

    for i in range(N):
      for j in range(K+1):
        if(i == 0 and k != 0):
          if(j == a[i]): dp[i][j] = True
          continue
        elif(i == 1 and k == 0):
          if(j == a[i]): dp[i][j] = True
          continue
        elif(dp[i-1][j] == True):
          dp[i][j] = True
          continue
        elif(j - a[i] >= 0):
          if(dp[i - 1][j - a[i]] or dp[i - 1][j]): dp[i][j] = True
          else: dp[i][j] = False

        else:
          if(dp[i - 1][j]): dp[i][j] = True
          else: dp[i][j] = False
    a[k] = tmp
    for i in range(N):
      flag = False
      for j in range(K-a[k], K+1):
        if(dp[i][j] == True):
          ans += 1
          flag = True
          break
      if(flag):
        break


print(N - ans)

