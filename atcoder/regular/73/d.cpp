#include <iostream>
#include <vector>
#include <algorithm>
#include<math.h>



int main(void){

  long long N, W;
  std::cin>> N, W;
  long long w[104], v[104];

  long long tmp1;
  long long tmp2;
  long long a, b;
  for(int i = 0; i < N; i++){
    std::cin >> a, b;
    std::cout<< a, b << "\n";
    // w.push_back(tmp1);
    // v.push_back(tmp2);
  }
  //
  // long long dp[W+1][N+1];
  //
  // for(int i = 0; i < W+1; i++){
  //   for(int j = 0; j < N+1; j++){
  //     dp[i][j] = 0;
  //   }
  //  }
  //
  // for(int i = 0; i < W+1; i++){
  //   for(int j = 0; j < N+1; j++){
  //     if(j == 0){
  //       continue;
  //     }
  //     if(i - w[j-1] >= 0){
  //       dp[i][j] = std::max(dp[i][j-1], std::max(dp[i-w[j-1]][j-1] + v[j-1], dp[i][j]));
  //     }
  //     else{
  //       dp[i][j] = std::max(dp[i][j-1], dp[i][j]);
  //     }
  //   }
  // }
  //
  //
  //
  // std::cout<< dp[W][N] << "\n";
  // return 0;
}

//
// N, W = map(int, input().split())
// w = []
// v = []
//
// for _ in range(N):
//   tmp = input().split()
//   w.append(int(tmp[0]))
//   v.append(int(tmp[1]))

// dp = []
//
// for i in range(W+1):
//   dp.append([])
//   for j in range(N+1):
//     dp[i].append(0)
//
//
//
// for i in range(W+1):
//   for j in range(N+1):
//     if(j == 0):
//       continue
//     if(i - w[j-1] >= 0):
//       dp[i][j] = max(dp[i][j-1], dp[i-w[j-1]][j-1] + v[j-1], dp[i][j])
//     else:
//       dp[i][j] = max(dp[i][j-1], dp[i][j])
// print(dp[W][N])