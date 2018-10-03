#include <stdio.h>
#include <vector>

int main(void){

    int val;
    std::vector<int>v; std::vector<int>::iterator iter;
    printf("Digite alguns inteiros:");
    do{
        scanf("%d", & val);
        v.push_back(val);

    }
    while(val!= -1);
    for(iter = v.begin(); iter != v.end(); iter++)
        printf("%d", *iter);



}
