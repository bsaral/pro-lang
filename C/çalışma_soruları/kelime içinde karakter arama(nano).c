#include <stdio.h>
#include <string.h>
#include <ctype.h>

int kelime_ara(char s[]){
    int i;
    char n[100];
    char k[100];
    int state=0;
    for (i=0;i<=strlen(s);i++){
        switch(state){
                      case 0:
                           k[i]=s[i];
                           state=1;
                           
                      case 1:
                           if (s[i]=='n'){
                                          n[0]=s[i];
                                          state=2;
                                          }
                           else
                           state=0;
                          
                           
                      
                      case 2:
                           if (s[i]=='a'){
                                          n[1]=s[i];
                                          state=3;
                                          }
                           else
                           state=0;
                          
                          
                           
                      case 3:
                           if (s[i]=='n'){
                                          n[2]=s[i];
                                          state=4;
                                          }
                           else
                           state=0;
                          
                           
                           
                      case 4:
                           if (s[i]=='o'){
                                          n[3]=s[i];
                                          break;
                                          
                                          }
                           else
                           state=0;
                           
                           
                           }
                           }
        if (strlen(n)==4){
                       printf("\ntrue");}
        else {
             printf("\nfalse");}
        
        
        
        }
                           
                                          
                                          




int main(void){
    kelime_ara("banananana");
    kelime_ara("banananano");
    kelime_ara("nnnnnnnanofff");
    
    
    getch();
}
