package cap03;
import javax.swing.JOptionPane;

import com.sun.org.apache.bcel.internal.generic.BREAKPOINT;

public class question01 {
	public static void main(String args[]){
	String aux;
	float desconto, farea, perimetro ;
	try {
		String nome = JOptionPane.showInputDialog(null, "Digite o nome do produto:");
		float flutuante;
		flutuante = 0;
		float valor = (float) Double.parseDouble(JOptionPane.showInputDialog("insira o valor: "));
		
		if(valor < 0){
			JOptionPane.showMessageDialog(null, "Valor menor que zero");
			
			
		}
		else{
		if (valor >= 50 && valor <200){
			flutuante = 5;
					
					
		}

		if (valor >= 200 && valor <500){
			flutuante = 6;
					
					
		}

		if (valor >= 500 && valor < 1000)
		{
			flutuante = 7;
					
					
		}

		if (valor >= 1000){
			flutuante = 8;
					
					
		}
		
		valor = valor - (flutuante * valor)/100	;
		
		
		JOptionPane.showMessageDialog(null, "Valor com desconto: " + valor);
	}}
	catch (NumberFormatException erro){
		
		JOptionPane.showMessageDialog(null,"Houve um erro na conversao, digite apenas caracteres numericos" + erro.toString());
		
		
	}
	
	

	}

}