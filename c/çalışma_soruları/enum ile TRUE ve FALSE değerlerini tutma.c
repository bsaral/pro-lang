#include <stdio.h>
#include <ctype.h>
main(){
       enum durumlar {TRUE,FALSE};
       int c;
       enum durumlar durum = TRUE;
       while (c !=EOF){
             c=getchar();
             switch (durum){
                    case TRUE :
                         if (islower(c)){
                                         printf("true");
                                         durum=FALSE;
                                         }
                                         break;
                                         
                    case FALSE :
                         if (isupper(c)){
                                         printf("False");
                                         durum=TRUE;
                                        
                                         }
                                         break;
                                         }
                                         }
                                         getch();
                                         }
             
