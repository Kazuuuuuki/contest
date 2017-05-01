
#include <iostream>
#include <vector>
#include <algorithm>
#include<math.h>



int main(void){

  long long n;
  unsigned long long a = pow(10,9);
  std::cin>> n;
  unsigned long long ans = 1;
  for(long long i=1; i< n+1; i++){
    ans = ans*i;
    if(ans > a + 7){
      ans %=  (a + 7);
    }
  }
  std::cout<< ans % (a + 7) << "\n";
  return 0;
}
