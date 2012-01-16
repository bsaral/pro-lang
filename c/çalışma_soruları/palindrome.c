#include <stdio.h>
#include <string.h>

void ispalindrome(char* s){
     int i=0;int son;
     for (i;i<strlen(s)/2;i++){
         if (s[i]==s[strlen(s)-i-1]){
                                     son=1;}
         else {
              son=0;}
              }
         if (son==1){
                     printf("\ndogru");}
         else {
              printf("\nyanlis");}
              
              }
     
                                 
int main(void){
    ispalindrome("radar");
    ispalindrome("kabak");
    ispalindrome("yimirta");
    getch();
}
                                 
