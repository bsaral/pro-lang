#include <stdio.h>
main(){
       char c;
       int sayi=0,toplam=0;
       while (1){
             c=getchar();
             if ((c>='0') && (c<='9')){
                         sayi+=1;
                         toplam+=c;
                          }
             else  
                  break;
                  
                  
             }
       printf("\ngirilen toplam sayi karakteri= %d ",sayi);
       printf("\ngirilen sayilarýn ascii toplami= %d ",toplam);
       getch();
       }
