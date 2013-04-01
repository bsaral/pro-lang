/* BETÜL SARAL -- 10060298
 * 
 * AÇIKLAMA : 
 * ok tuşları tarihçeyi göstermektedir.
 * /bin/ altında kendi dosyanızı oluşturursanız (örn:/bin/mycommnad) komut çalıştırılır aksi halde komut bulunamaz.
 * tarihçe >_: sonra enter a basıldığı zaman çalışmaya başlar. */

#include <ncurses.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <term.h>

#define PATH "/bin/"
	
int main(){
	FILE *dosya;
	FILE *read;
	FILE *command;
	int i;
	char rd[80];
	char ch[80];
	char *yol;
	yol  = (char * ) malloc(sizeof(char));
	dosya = fopen("shell_history.txt","a");
	if(dosya == NULL )
		printf("history dosyası açılmadı !!!");
	
	initscr();
	keypad(stdscr,TRUE);
	
	while(1){
		
		i = getch();
		read = fopen("shell_history.txt","r");
		while ((i == KEY_UP) && (!feof(read))){
			if (read == NULL )
				printw("dosya açılmadı");
			else {
				fscanf(read,"%s",rd);
				printw("\n%s",rd);
				i = getch();
			}
		}
		
		printw("\n>_: ");
		getstr(ch);
	
		if(strcmp(ch,"quit")){
			fprintf(dosya,"%s\n",ch);
			strcat(yol,PATH);
			strcat(yol,ch);
			command = fopen(yol,"r");
			if( command == NULL ){
				printw("komut bulunamadı");
				printw("\n%s",yol);
			}
			else
				printw("komut çalıstırıldı");
		}
	
		else
			exit(1);
		}
	
	endwin();
	return 0;
}


