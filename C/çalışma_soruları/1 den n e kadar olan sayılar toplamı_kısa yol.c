#include<stdio.h>
#define toplam(n) (n*(n+1))/2

int main(){
    int n;
    printf("ust deger giriniz : ");
    scanf("%d",&n);
    printf("%d",toplam(n));
    getch();
}
    
