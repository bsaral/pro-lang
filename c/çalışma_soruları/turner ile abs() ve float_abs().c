#include <stdio.h>
int abs(int n){
    
   return (n>=0)?n:(-1)*n;
    
}


int float_abs(float n){
    
    float z;
    z=(n>=0)?n:(-1.0)*n;
    printf("%.2f",z);
}



int main(){
    int a;
    float b;
    printf("\nbir sayi giriniz (negatif/pozitif) : ");
    scanf ("%d",&a);
    printf("\n%d",abs(a));
    printf ("\nondalik sayi giriniz : (neg/poz): ");
    scanf("%f",&b);
    float_abs(b);
    getch();
}
              
