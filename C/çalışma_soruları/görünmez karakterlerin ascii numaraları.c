#include <stdio.h>
main(){
       char c;
       while (c!=EOF){
             c=getchar();
             if ((c>=0) && (c<=32)){
                        printf("\ngorunmez karakter numarasi: %d \n",c);
                       
                        }
             else {
                  putchar(c);
                  }
                  }
       getch();
       }
       
       
      
