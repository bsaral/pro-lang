#include <stdio.h>
int main(void)
{
    char a;
    printf("istedi�iniz karakteri buraya giriniz : ");
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
                         
