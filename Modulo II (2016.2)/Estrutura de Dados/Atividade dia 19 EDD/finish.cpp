#include <stdio.h>
#include <stdlib.h>

int lista[int tamanhoDaLista];
tamanhoDaLista = 5;
int ultimo = 0;
int primeiro = 0;

void inserirFinal(int novo){
    if(ultimo < tamanhoDaLista){
        lista[ultimo] = novo;
        ultimo++;
    }
    else
        printf("LISTA LOTADA !!");

}

void removerInicio(){
    int i;
    for (i=0 ; i<ultimo; i++){

            lista[i] = lista[i+1];
       }
        ultimo -= 1;

        printf("Ultimo: %d\n", ultimo);
}
void consultaProximo(){
    int i;
    int informeNumero = -1;
    printf("Digite um numero");
    scanf("%d",& informeNumero);
    bool j = false;
    for (i=0 ; i<ultimo; i++){


            if (lista[i] == informeNumero){
                if (i == ultimo - 1){
                    j = true;
                    printf("Esse numero eh o ultimo!!");}


                else{
                printf("O proximo é: %d", lista[i + 1]);
                j = true;
                printf("\nultimo: %d esse e o i : %d" , ultimo,i
                );
               }
            }


     }
       if (j == false){
        printf("O Elemento nao esta na lista!!");
       }
       }


main() {
    int i;

    inserirFinal(1);
    inserirFinal(3);

    lista[0];

    for (i=0 ; i<5; i++){

       printf("%d\n", lista[i]);
    }

}
