package domain;



public class EmpresaNovo {

	public static void main(String[] args) {
		String nomeEmpresa;
		String cnpj;
		String nome;
		double salario;
		String dataEntrada;
		String rg;
		FuncionarioNovo [] arrayFuncionarios = new FuncionarioNovo[10];
		FuncionarioNovo f1 = new FuncionarioNovo("joao");
		inserir(arrayFuncionarios, f1);
		

		System.out.println(arrayFuncionarios[0].getNome());
		
		
		
		
	}
	public static void inserir(FuncionarioNovo[] funcionario,  FuncionarioNovo n){
	for(int v = 0; v < 10; v++){
		if(funcionario[v] == null){
			
			funcionario[v] = n;
		
		}
		
	}
		
		
		
		
	}}
