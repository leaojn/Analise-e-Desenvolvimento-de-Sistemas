package cap02;
import javax.swing.JOptionPane;

public class Question4 {
	public static void main(String args[]){
	String aux;
	float nota1 , nota2, nota3, media;
	try {
		aux = JOptionPane.showInputDialog("Nota 1(Prova):");
		nota1 =  Float.parseFloat(aux);
		
		aux = JOptionPane.showInputDialog("Nota 2(Prova):");
		nota2 =  Float.parseFloat(aux);
		
		aux = JOptionPane.showInputDialog("Nota 3(Trabalho):");
		nota3 =  Float.parseFloat(aux);
		media = (nota1 + nota2 + nota3) / 3;
		
		if (media >= 6){
			JOptionPane.showMessageDialog(null, "Aprovado");
			
		}
		else{
			JOptionPane.showMessageDialog(null, "Reprovado");
		}
		
		
	}
	catch (NumberFormatException erro){
		
		JOptionPane.showMessageDialog(null,"Houve um erro na conversao, digite apenas caracteres numericos" + erro.toString());
		
		
	}
	
	

	}

}