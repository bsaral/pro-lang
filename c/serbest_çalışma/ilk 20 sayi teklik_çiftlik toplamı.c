#include <stdio.h>
main ( )
{
     int i,c,t;
     c=0;t=0;
     for (i=1;i<=20;i++)
     {
         if (i%2==0)
         {
                    c=c+i;
     
         }
         else
         {
             t=t+i;

             }
             
             }
     printf("cift sayilar toplami : %d",c);
     printf("\ntek sayilar toplami : %d",t);
         
         

getch();
}
                         
