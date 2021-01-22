#include <stdio.h>
int main () {
    int a, k=0;
    for(int i=1; i<=5; i++){
        scanf("%d", &a);
        if(a % 2 == 0){
            k++;
        }
    }
    printf("%d valores pares\n", k);
  return 0;
}