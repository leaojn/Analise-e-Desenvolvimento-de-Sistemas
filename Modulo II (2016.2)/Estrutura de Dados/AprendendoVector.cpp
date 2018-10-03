#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;







main(){

    vector<int> V;
    V.push_back(1);
    V.push_back(2);
    V.push_back(3); // Line 1
    V.insert(V.begin(), 20); // Line 2
    V.insert(V.begin() + 2, 30); // Line 3
    V.insert(V.end(), 40); // Line 4
    vector<int>::iterator Iter = V.end() - 1;
    int numero = *Iter;
    printf("%d\n", numero);
    for(int i = 0; i <= V.size();i++){
        printf("Posição%d Numero:%d\n", (i+1),V[i]);

    }


}
