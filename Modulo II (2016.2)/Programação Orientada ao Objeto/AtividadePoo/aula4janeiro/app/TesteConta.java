package app;
import domain.Conta;

public class TesteConta {

	
	public static void main(String[] args) {
		Conta conta = new Conta();
		conta.titular = "Rogerio Silva";
		conta.saldo = 17500;
		System.out.println(conta.toString());
		
		
	}

}
