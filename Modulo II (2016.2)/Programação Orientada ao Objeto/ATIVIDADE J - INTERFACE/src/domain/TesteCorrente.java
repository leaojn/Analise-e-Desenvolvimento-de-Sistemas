package domain;

public class TesteCorrente {

	public static void main(String[] args) {
		ContaCorrente nova = new ContaCorrente("Joao", 2, 1000);
		nova.deposito(200);
		System.out.println(nova.status());
	}

}
