package cap02;
import javax.swing.JOptionPane;

public class Question3 {
	public static void main(String args[]){
	String aux;
	float transacao, venal, percentual, imposto , flutuante;
	try {
		aux = JOptionPane.showInputDialog("Valor venal:");
		venal =  Float.parseFloat(aux);
		
		aux = JOptionPane.showInputDialog("Valor de transacao:");
		transacao =  Float.parseFloat(aux);
		
		aux = JOptionPane.showInputDialog("Valor percentual:");
		percentual =  Float.parseFloat(aux);
		
		if (venal >= transacao){
			flutuante = venal;
		}
		else{
			flutuante = transacao;
		}
		
		imposto = flutuante * percentual / 100;
		JOptionPane.showMessageDialog(null, "Valor do imposto: " + imposto + ", Valor com o imposto:" + (flutuante+ imposto));
	}
	catch (NumberFormatException erro){
		
		JOptionPane.showMessageDialog(null,"Houve um erro na conversao, digite apenas caracteres numericos" + erro.toString());
		
		
	}
	
	

	}

}