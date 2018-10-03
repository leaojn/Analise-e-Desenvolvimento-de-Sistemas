package cap03;

import javax.swing.JOptionPane;

public class question5{

	public static void main(String[] args) {
		
		
		String comeco = JOptionPane.showInputDialog("Escolha o exercicio: \n1-primeiro \n2-segundo \n3-terceiro \n4-quarto");
		
		
		switch (comeco) {
		case "1":
			question01.main(null);
			break;
		case "2":
			question2.main(null);
		case "3":
			question03.main(null);
		case "4":
			questio04.main(null);
		default:
			break;
		}
	}

}