#include <iostream>
#include <vector>
using namespace std;
//questao 1 = letra b;
//questao 2 = letra b;
class No{
  private:
	int codigo;
	string letra;
 public:
	No(int c, string l){
		codigo=c;
		letra=l;
	}
	void mostra(){
        cout<<"Letra: "<<this->letra<<" Codigo: "<<this->codigo<<endl;
	}
	int getCodigo(){
        return this->codigo;
	}

};

class Lista{
	private:
        vector<No> l;
	public:
        void setInserir(string elemento, int codigo){
            No aux(codigo, elemento);
            l.push_back(aux);
        }
        void furaFila(int posicao,string elemento, int codigo){
            vector<No>::iterator i = l.begin();
            No aux2(codigo, elemento);
            l.insert(i+posicao, aux2);
        }
        void mostra(){

            for(int i = 0; i < l.size();i++){
                l[i].mostra();
            }
        }
        void remover(int codigoElemento){
            int checkElemento = 0;
            for(vector<No>::iterator i = l.begin(); i != l.end();i++){
                if(i->getCodigo() == codigoElemento){
                    checkElemento++;
                    l.erase(i);
                }
            }
            if(checkElemento == 0)
                cout<<"Elemento n existe"<<endl;
        }

};

int main(){
    Lista *l1 = new Lista();

    l1->setInserir("m",1);
    l1->setInserir("a",2);
    l1->setInserir("i",3);
    l1->setInserir("o",4);
    l1->furaFila(2,"r",5);
    l1->mostra();
    l1->remover(6);
    cout<<"\n\n";
    l1->mostra();
}
