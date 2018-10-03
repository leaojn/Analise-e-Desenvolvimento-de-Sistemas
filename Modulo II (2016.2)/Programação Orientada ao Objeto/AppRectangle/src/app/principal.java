package app;
import java.util.jar.JarOutputStream;
import javax.swing.JOptionPane;
import domain.Rectangle;

public class principal {
	public static void main(String[] args){
	
		String menu = "###### RT ######";
		menu += "\n 1 - Configurar Rectangle 1";
		menu += "\n 2 - Configurar Rectangle 2";
		menu += "\n 3 - Sair. \n";
		
		Rectangle rect = new Rectangle();
		Rectangle rect2 = new Rectangle();
		
		int op = -1;
		
		while(op != 0){
			
			op = showMensage(menu;)
			switch (op){	
				case 1:
					
					//Config do rect1
					rect1.width = 
					break;
					
				case 2:
					//Config do rect2
					break;
					
				
			}
		}
	}


	private static void showMensage(String menu) {
		JOptionPane.showInputDialog(menu);
	}

	
	public static void main(String[] args) {
		
		Rectangle rect1 = rect();
		
		
		rect1.width = 100;
		JOptionPane.showMessageDialog(null,"Ok. Area: " + rect1.area());
	}


	private static Rectangle rect() {
		String entrada;
		Rectangle rect1 = newRectangle();
				
		entrada = JOptionPane.showInputDialog("W: ");
		rect1.width = Double.parseDouble(entrada);
		return rect1;
	}


	private static Rectangle newRectangle() {
		Rectangle rect1 = new Rectangle();
		String entrada	= JOptionPane.showInputDialog("H: ");
		rect1.height = Double.parseDouble(entrada);
		return rect1;
	}

}	
	private static Double getDouble(String msg)
