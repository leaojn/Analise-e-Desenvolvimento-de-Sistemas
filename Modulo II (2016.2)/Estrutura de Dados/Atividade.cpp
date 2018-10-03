#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;

char * menu(){


    return "**********Menu**********\n1- inserir\n2- remover\n3- Consultar\n4- Alterar.\n";


}


void inserir(){



}
main(){

    int numero = -1;
    while(numero != 0){

        printf(menu());
        printf("Digite a opção:");
        scanf("%d" ,& numero);

        if (numero == 1){
            inserir();

        }
        }


}
