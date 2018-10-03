package modelo;

public abstract class Aluno {
	
	private final int QTD_NOTAS = 3;
	
	private String nome;
	private int matricula;
	protected double[] notas;
	
	public Aluno(String nome, int matricula) {
		this.nome = nome;
		this.matricula = matricula;
		this.notas  = new double[QTD_NOTAS];
	}
	
	protected abstract Object[] media();
	
	public String getSituacao(){
		if (media() >= 6){
			return "APROVADO";
		}else{
			return "REPROVADO";
		}
	}
	
	public double[] getNotas() {
		return notas;
	}
	
	public final String toString() {
		return this.nome + String.format(" Media: %.2f", media()) + " Situacao: " + getSituacao();
	}


}