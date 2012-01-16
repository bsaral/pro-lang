#include <stdio.h>
#include <math.h>
main(void)
{
      int a,b,c,delta,x1,x2;

      printf("ax*2+bx+c denkleminin katsayýlarýný giriniz (a,b,c) : ");
      scanf("%d,%d,%d",&a,&b,&c);
      delta=b*b-4*a*c;
      if (delta >0){
                x1 = (-b + sqrt(delta)) / (2 * a);
                x2 = (-b - sqrt(delta)) / (2 * a);
                printf("x1 = %d, ax2 = %d",x1,x2);
                if (delta==0){
                    x1=-b/(2*a);
                    
                    printf("tek kökü vardýr. x1 = %d",x1);
                    }
                }
      
      else{
          printf("denklemin kökü yoktur.");
           }
           
      getch();
}
                    
                         
   
