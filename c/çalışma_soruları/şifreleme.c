#include <stdio.h>
main(){
       char b;
       while (b != EOF){
             b=getchar();
             if ((b>='A' && b<='Z') || (b>='a' && b<='z'))
             {
                         b=b+2;
                         putchar(b);
                         }
             else if ((b>='0') && (b<='9'))
             {
                  
                  b+=13;
                  putchar(b);}
                  }
             return 0 ;
                  }
                         
