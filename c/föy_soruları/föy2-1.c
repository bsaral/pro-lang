#include <stdio.h>
int main(void) {
int c;
for ( ; ; ) {
c = getchar();
putchar(isupper(c)?tolower(c):toupper(c));

}
return 0;
}
                    
                         
