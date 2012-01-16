#include <stdio.h>
#include <string.h>

void max(int *p,int n){
     int i=0;
     for(i;i<=n;i++){
                    if (p[i]>p[i+1]){
                                     printf("%d\n",p[i]);}
                                     }
}
int sayi[5]={1, 1, 2, 3, 4};
int main(void){
    max(sayi,5);
    getch();
}
     
