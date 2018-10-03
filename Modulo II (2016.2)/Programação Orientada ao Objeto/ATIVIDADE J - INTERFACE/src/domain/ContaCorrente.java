package domain;

public class ContaCorrente implements Conta {
	private int numeroConta;
	private String nome;
	private double saldo;
	private int cpf;

	public ContaCorrente(String nome, int numeroConta, double saldo){
		
		this.nome = nome;
		this.numeroConta = numeroConta;
		this.saldo = saldo;
		
		
		
	}

	public double saldo() {
		return this.saldo;
	}
	//Verificação se os valores sao possiveis com o exception

	public double saque(double retirada) {
		return this.saldo -= retirada;
		
	}
	//Verificação se os valores sao possiveis com o exception
	public double deposito(double entrada) {
		return this.saldo = this.saldo + entrada;
		
	}

	public double status(){
		return this.saldo;
		
	}

	public int getNumeroConta() {
		return numeroConta;
	}

	public void setNumeroConta(int numeroConta) {
		this.numeroConta = numeroConta;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public double getSaldo() {
		return saldo;
	}

	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}

	public int getCpf() {
		return cpf;
	}

	public void setCpf(int cpf) {
		this.cpf = cpf;
	}
	


}

