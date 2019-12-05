#include <stdio.h>

int main(int argc, char **argv) {
  long p, q, s;

  scanf("%ld %ld %ld", &p, &q, &s);
  int i = 1;
  while(i <= s) {
    if (i % p == 0 && i % q == 0) {
      printf("true, %d\n", i);
      return 0;
    }  
    i++;
  }
  printf("false");
  return 1;
}

