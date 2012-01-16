#include <stdio.h>
main(){
       char c;
       while (1){
             c=getchar();
             if ((c>=48) && (c<=57)){
                        putchar(c);
                        
                        }
             else if((c>=65) && (c<=125)) {
                  char c='*';
                  printf ("%c",c);
                  

                  }
                  }
       return 0;
       }
       
       
      
