package cap03;
import javax.swing.JOptionPane;

import com.sun.org.apache.bcel.internal.generic.BREAKPOINT;

public class question2 {
	public static void main(String args[]){
	String aux;
	int r1, r2, r3,r4,equivalente , maior, menor;
	maior = 0;
	menor = 0;
	try {
		aux = JOptionPane.showInputDialog("R1: ");
		r1 =  Integer.parseInt(aux);
		
		aux = JOptionPane.showInputDialog("R2: ");
		r2 =  Integer.parseInt(aux);
		
		aux = JOptionPane.showInputDialog("R3: ");
		r3 =  Integer.parseInt(aux);
		
		aux = JOptionPane.showInputDialog("R4: ");
		r4 =  Integer.parseInt(aux);
		equivalente = r1 + r2 + r3 + r4;
		
		
		if (r1>=r2 && r1>=r3 && r1>=r4){
			maior = r1;
		}

		if (r2>=r1 && r2>=r3 && r2>=r4){
			maior = r2;
		}

		if (r3>=r1 && r3>=r2 && r3>=r4){
			maior = r3;
		}

		if (r4>=r1 && r4>=r2 && r4>=r3){
			maior = r4;
		}

		if (r1<=r2 && r1<=r3 && r1<=r4){
			menor = r1;
		}

		if (r2<=r1 && r2<=r3 && r2<=r4){
			menor = r2;
		}

		if (r3<=r1 && r3<=r2 && r3<=r4){
			menor = r3;
		}

		if (r4<=r1 && r4<=r2 && r4<=r3){
			menor = r4;
		}
		
	JOptionPane.showMessageDialog(null, "Resistencias Fornecidas" + "\n" + r1+ "," + r2+"," + r3+ "," + r4+  "\n"+ "A maior resistencia é:" + maior + "\n" + "A menor resistencia é:" + menor);
	}
	catch (NumberFormatException erro){
		
		JOptionPane.showMessageDialog(null,"Houve um erro na conversao, digite apenas caracteres numericos" + erro.toString());
		
		
	}
	
	

	}

}