#include <stdio.h>
main(){
       enum cinsiyet{kiz,erkek};
       char c;
       enum cinsiyet cins=kiz;
       while (c !=EOF){
             c=getchar();
             switch(cins){
                          case kiz :
                               if ((c=='k')|| (c=='K')){
                               printf("kiz\n");
                               cins=erkek;
                               }
                               break;
                          case erkek:
                               if ((c=='E') || (c=='e')){
                                            printf ( "erkek\n");
                                            cins = kiz;
                                            }
                                            break;
                                            }
                                            }
                                            getch();
                                            }
                          
