#include <stdio.h>

main(void){
           char c;
           
           while (1){
                 c=getchar();
                 if((c>='a')&&(c<='z')){
                                        c=c-32;
                                        putchar(c);
                                        
                                        }
                 else
                 putchar(c);
                 }
                 getch();
                 }
