#include <stdio.h>
#include <math.h>
main(){
int i;
printf ("  n\t\t2^n\n ------------------- ");
for (i=0;i<=16;i++){
    printf("\n  %d \t\t%.f",i,pow(2,i));
    }
    return 0;
getch();

}
