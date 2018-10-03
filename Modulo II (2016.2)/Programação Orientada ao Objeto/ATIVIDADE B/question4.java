package balancoTrimestral;

public class BalancoTrimestral {

	
	public static void main(String[] args) {
		int gastosJaneiro = 15000;
		int gastosFevereiro = 23000;
		int gastosMarco = 17000;
		int gastosTrimestre = gastosJaneiro + gastosFevereiro + gastosMarco;
		System.out.println("Gastos Trimestrais:" + gastosTrimestre + "\n" + "Valor da media mensal:" + gastosTrimestre/2);
		

	}

}
