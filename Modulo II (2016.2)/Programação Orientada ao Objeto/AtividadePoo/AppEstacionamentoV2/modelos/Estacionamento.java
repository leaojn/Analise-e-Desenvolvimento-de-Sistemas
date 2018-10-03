package modelos;

public class Estacionamento {
	private static Estacionamento estacionamento;
	
	private String nome;
	private VeiculoV [] vagas;
	
	
	private Estacionamento(){
		
		
		
	}
	
	public static Estacionamento getInstance(){
		if(estacionamento == null)
			Estacionamento.estacionamento = new Estacionamento();
		return estacionamento;
	}
	public boolean entrada(Veiculo veiculo){
		
		for (iterable_type iterable_element : iterable) {
			
		}
	}
}
