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
             printf("\ntoplam karakter sayisi : %d",(a-1)); //line feed k�sm�n� ��kartt�k.(space k�sm� ekli)
             printf("\ntoplam kelime sayisi : %d",(b+1));  //bir karakter dizisinde bo�luk say�s�n�n bir fazlas� kadar kelime bulunur.

             getch();
             }
             
                  
                   
