#include <stdio.h>
#include <ctype.h>
main(){
       int i;
       char c;
       while(c != 10){
               c=getchar();
            if (c=='a' || c=='e'||c=='�'||c=='i'||c=='o'||c=='�'||c=='u'||c=='�')  
            {
                          if (islower(c)){
                                             putchar(toupper(c));
                                             
                                             }
                          else
                          putchar(c);
                          
                          }
                                             
            else
            putchar(c) ;
            
            
       }
       getch();
       }
             
             
                  
                   
