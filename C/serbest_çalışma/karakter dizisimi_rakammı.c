#include <stdio.h>
int main(void)
{
    char a;
    printf("istediðiniz karakteri buraya giriniz : ");
    scanf("%s",&a);
if ((a>='1') && (a<='9'))
{
             printf("rakamdir.");
}
else 
{
     printf ("karakter dizisidir.");
}

getch();
}           
                         
