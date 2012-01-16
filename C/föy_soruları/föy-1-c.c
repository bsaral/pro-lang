#include <stdio.h>
int main(){
       int alt,ust,i;
       printf("alt siniri giriniz : ");scanf("%d",&alt);
       printf("\nust siniri giriniz : ");scanf("%d",&ust);
       for (i=alt;i<=ust;i++)
       {
           printf("%3d",i);
       }
       printf("bu kdr");
       
       getch();
}
