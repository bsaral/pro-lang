#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void){
    char sayi[100];
    int i;int say=0;int toplam=0;
    char n;
    
    printf("octal tabanindaki sayiyi giriniz : ");
    scanf("%s",sayi);
    
    for (i=0;i<strlen(sayi);i++){
        n=sayi[strlen(sayi)-1-i]-'0';
        
        if (n==8 || n==9){
                 printf("bu sayi octal tabaninda degil.\n");
                 break;}
                 
        say=n*pow(8.0,i);
        toplam=toplam+say;
        
        }
        printf("%d",toplam);
        getch();
        }
