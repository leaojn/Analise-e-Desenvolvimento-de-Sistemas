#include <iostream>
#include <string>
using namespace std;

class Cliente{
	private:
		string nome;
		int numcartao;
		float saldo;
		float limite;
	public:
		Cliente(string nome,int n,float s,float l){
			this->nome=nome;
			this->numcartao=n;
			this->saldo = s;
			this->limite =l;
		}
		string getNome(){
			return this->nome;
		}
		float getSaldo(){
			return this->saldo;
		}
		float getLimite(){
			return this->limite;
		}
};

class Lista{
	private:
	   Cliente *lista[5];
	   int quant;
	public:
	 Lista(){
		quant=0;
	}
	void inserir(string nome,int n,float s,float l){
		if (quant<5){
			Cliente *novo=new Cliente(nome,n,s,l);
			lista[quant]=novo;
			quant++;
		}
		else 
			cout<<"LISTA LOTADA!!!";
		
	}
	
	void mostrar(){
		for(int i=0;i<quant;i++){
			
		}
		
	}
	
	Cliente *menorSaldo(){
		
	}
	Cliente *maiorLimite(){
		
	}
};

main(){
	Lista *l1=new Lista();
	l1->inserir("Joao",1 ,10.2,100);

	
}
