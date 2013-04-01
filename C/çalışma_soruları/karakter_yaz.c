#include <string.h>
#include <ncurses.h>

int main() {
    int ch;
    char buffer[256];
    initscr(); cbreak(); noecho();
    keypad(stdscr, TRUE);
    
    while ( (ch = getch()) == ERR );
    sprintf(buffer,"key 0x%02X was pressed\n\n", ch);
    addstr(buffer);
    addstr("press any key to exit.");
    while ( (ch = getch()) == ERR );
    endwin();
}
