#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int i;
	for(i=1; i<12; i +=1){
		printf("Hola %d\n",i);
	}
	int x;
	for ( x=0; x<6; x+=1){
		printf("\n");
			int k;
		for(k=0;k<10;k+=1){
			if (x==0 || x==5 ||k==0 ||k==9) 
			   printf("#");
		    else{
		       	printf(" ");
			   }
		
		}
	
		
	}
	return 0;
}
/*
#####
####
###
##
#


#
##
###
####
#####
######


######
 #####
  ####
   ###
    ##
     #
/
