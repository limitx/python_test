#include <stdio.h>
#include "Utils.h"

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	Utils utils;
	
	utils.loadkeys();
	utils.loadfile();
	utils.search();
	return 0;
}
