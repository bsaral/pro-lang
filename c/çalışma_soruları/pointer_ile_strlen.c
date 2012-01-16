#include <stdio.h>
#include <string.h>

void say(char* s){
     int i;int a=0;
     for (i=0;i<strlen(s);i++){
         a=a+1;
         if (s[i]=='\0')
         break;
                         }
     printf("%d",a);
     }
         
     
int main(void){
    say("betul saral");
    getch();
}
                                 
