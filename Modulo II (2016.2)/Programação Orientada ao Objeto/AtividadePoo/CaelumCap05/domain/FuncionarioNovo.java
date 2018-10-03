package domain;

import app.app;

public class FuncionarioNovo{


	private String nome;
	private double salario;
	private String dataEntrada;
	private String rg;
	//Construtor
	public FuncionarioNovo(String nome){
		this.nome = nome;
	}
	
	public void recebeAumento(int aumento){
		salario += aumento;
		
				
	}

	public void status(){
		System.out.println("Nome: " + nome);
		System.out.println("Salario: " + salario);
		System.out.println("Data de entrada: " + dataEntrada);
		System.out.println("RG: " + rg);
		
		app.comparacao();
		
		
		
		
		
	}
	

	

	

	

	public String getNome() {
		return nome;
	}

	public  double getSalario() {
		return salario;
	}

	public String getDataEntrada() {
		return dataEntrada;
	}

	public String getRg() {
		return rg;
	}

	


}