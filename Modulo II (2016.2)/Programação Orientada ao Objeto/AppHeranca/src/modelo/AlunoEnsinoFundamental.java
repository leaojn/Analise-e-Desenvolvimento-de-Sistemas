package modelo;

public class AlunoEnsinoFundamental extends Aluno{
	
	private boolean podeSairSo;
	
	public AlunoEnsinoFundamental(String nome) {
		this(nome, -1);
	}
	
	public AlunoEnsinoFundamental(String n, int mat) {
		super(n, mat);
		this.podeSairSo = false;
	}
	
	
	protected double media() {
		double med = (notas[0] + notas[1] + notas[2])/3;
		return med;
	}
}