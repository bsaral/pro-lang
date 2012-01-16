#include<stdio.h>

int cevir_hex(int n){
    printf("\nsayinin hexadecimal degeri : ");
    printf("%x",n);
}


int cevir_octal(int n){
    printf("\nsayinin octal degeri :  ");
    printf("%o",n);
}


int cevir_binary(int n){
    
    int i=0;int k[30];
    while(n>=1){
                i+=1;
                k[i]=n%2;
                n=n/2;
                }
    printf("\nsayinin binary degeri: ");
    for (i;i>0;i--){
        printf ("%d",k[i]);
        }
        }
        


int main(void){
    int n;
    printf ("\nbir sayi giriniz : ");
    scanf("%d",&n);
    cevir_binary(n);
    cevir_octal(n);
    cevir_hex(n);
    getch();
    }
        
