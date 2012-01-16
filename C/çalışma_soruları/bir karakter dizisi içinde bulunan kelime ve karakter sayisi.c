#include <stdio.h>
main(){
       int a=0,b=0,d=0;
       char c;
       while (c != 10){ 
             c=getchar();
             a=a+1;
             if (c==32){
                        b=b+1;
                        }
                  }
             printf("\ntoplam karakter sayisi : %d",(a-1)); //line feed kýsmýný çýkarttýk.(space kýsmý ekli)
             printf("\ntoplam kelime sayisi : %d",(b+1));  //bir karakter dizisinde boþluk sayýsýnýn bir fazlasý kadar kelime bulunur.

             getch();
             }
             
                  
                   
