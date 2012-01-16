#include <stdio.h>
main(){
       int ay,gun,s;
       printf("tarihi giriniz(gun/ay) : ");
       scanf("%d/%d",&gun,&ay);
       switch (ay){
              case 12:
                   s=365-(31-gun);
                   printf("yilin %d. gunu",s);
                   break;
              case 11 :
                   s=365-31-(30-gun);
                   printf("yilin %d. gunu",s);
                   break;
              case 10 :
                   s=365-31-30-(31-gun);
                   printf("yilin %d. gunu",s);
                   break;
              case 9 :
                   s=365-31-30-31-(30-gun);
                   printf("yilin %d. gunu",s);
                   break;
              case 8 :
                   s=365-31-30-31-30-(31-gun);
                   printf("yilin %d. gunu",s);
                   break;
              case 7 :
                   s=365-31-30-31-30-31-(31-gun);
                   printf("yilin %d. gunu",s);
                   break;
              case 6 :
                   s=365-31-30-31-30-31-31-(30-gun);
                   printf("yilin %d. gunu",s);
                   break;
              case 5 :
                    s=365-31-30-31-30-31-31-30-(31-gun);
                   printf("yilin %d. gunu",s);
                   break;
              case 4 :
                   s=365-31-30-31-30-31-31-30-31-(30-gun);
                   printf("yilin %d. gunu",s);
                   break;
              case 3 :
                   s=365-31-30-31-30-31-31-30-31-30-(31-gun);
                   printf("yilin %d. gunu",s);
                   break;
              case 2 :
                   s=365-31-30-31-30-31-31-30-31-30-31-(28-gun);
                   printf("yilin %d. gunu",s);
                   break;
              case 1 :
                   s=365-31-30-31-30-31-31-30-31-30-31-28-(31-gun);
                   printf("yilin %d. gunu",s);
                   break;
                   }
                   getch();
                   }
              
                   
       
       
       
