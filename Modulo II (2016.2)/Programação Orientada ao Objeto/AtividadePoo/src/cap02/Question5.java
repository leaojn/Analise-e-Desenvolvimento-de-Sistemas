package cap02;
import javax.swing.JOptionPane;

public class Question5 {
	public static void main(String args[]){
	String aux;
	float idade , sexo, anosDeContribuicao, flutuante;
	try {
		aux = JOptionPane.showInputDialog("Digite a idade:");
		idade =  Float.parseFloat(aux);
		
		aux = JOptionPane.showInputDialog("Digite 1 para M ou 2 para F:");
		sexo =  Float.parseFloat(aux);
		
		aux = JOptionPane.showInputDialog("Quantos anos de contribuição voce tem:");
		anosDeContribuicao =  Float.parseFloat(aux);
		
		
		if (sexo == 2 && idade >= 60 && anosDeContribuicao >= 30){
			JOptionPane.showMessageDialog(null, "Você pode se aposentar");
			
		}
		
		if (sexo == 1 && idade >= 65 && anosDeContribuicao >= 35){
			JOptionPane.showMessageDialog(null, "Você pode se aposentar");
			
		}
		else{
			JOptionPane.showMessageDialog(null, "Voce nao pode se aposentar");
		}
		
		
		
	}
	catch (NumberFormatException erro){
		
		JOptionPane.showMessageDialog(null,"Houve um erro na conversao, digite apenas caracteres numericos" + erro.toString());
		
		
	}
	
	

	}

}