#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int x;
	x=10;
	int y= 20;
    printf("Hola mundo en c\n");
    printf("Introduce un numero entero: ");
    scanf("%d",&y);
    printf("\tx vale :%d y Y vale:%d\a",x,y);
    	if (y>10) {
    		printf("\n %d es mayor que 10",y);
    }
    	if (y<10){
    		printf("\n %d es menor que 10",y);
    }
    	printf("\n con if - else");
    	if (y>10){
    		printf("\n %d es mayor que 10",y);
    }else{
    	printf("\n%d es menor que 10",y);
	}	
	
    printf("\nintroduce un valor entero entre 1 y 5: ");
    scanf("%d",&x);
    switch(x){
		case 1:
			printf("Hola\n");
			break;
		case 2:
			printf("Konichiwa\n");
			break;
		case 3:
			printf("Guten Tag\n");
			break;
	    case 4:
	    	printf("Hello\n");
	    	break;
	    case 5:
	    	printf("Namste");
	    	break;
	    default:
	    	printf("xico te falto un  numero");
	}
	return 0;
}
