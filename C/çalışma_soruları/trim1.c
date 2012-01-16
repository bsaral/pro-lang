#include <stdio.h>
#include <ctype.h>
#include <string.h>

int trim(char s[]){
    int i = 0;
    int state=1;
    for (i=0; i<=strlen( s);i++){
       switch(state){
                     case 1:
                          if (isspace(s[i])){
                                             printf("%c\b",s[i]);
                                             state=2;}
                          
                          
                     case 2:
                          if (isalpha(s[i])){
                                              putchar(s[i]);}
                          state=1;
                          
                          }
                          }
                          }

int main(){
    trim("            betul             ");
    getch(); 
}
    
