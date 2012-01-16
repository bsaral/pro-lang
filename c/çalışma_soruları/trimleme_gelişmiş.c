#include <stdio.h>
#include <ctype.h>
#include <string.h>

int trim(char s[]){
    int c;int i;
    int state=0;
    for (i=0; i<=strlen( s);i++){
       switch(state){
                          case 0:
                               if (isspace(s[i])){
                                             printf("%c\b",s[i]);
                                             state=1;}
                              
                          
                          case 1:
                               if(isalpha(s[i]) ){
                                            putchar(toupper(s[i]));
                                            state=2;}
                               else if (isspace(s[i])){
                                    state=0;}
                               else{
                                    putchar(s[i]);
                                    state=2;}
                                    break;
                              
                          case 2:
                               if(!isalpha(s[i]) && isspace(s[i])){
                                               state=0;}
                               putchar(s[i]);
                               
                                                           
                               }
                               }
                               }
                               
int main(){
    trim("         cos      217    rocks                ");
    getch(); 
}
                                    
