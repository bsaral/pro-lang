#include <stdio.h>
#include <string.h>
void fonks(char *);
     int main(void){
     char* s ="ghlabmmmcderrro";
     fonks(s);
}
void fonks(char *str){
     int say=0,i=1;
     for (i;i<strlen(str);i++){
         if (str[i]==str[i-1]){
            say+=1;
         if (say==2){
            printf("%c\n",str[i]);
     say=0;}
}
}
getch();
}




