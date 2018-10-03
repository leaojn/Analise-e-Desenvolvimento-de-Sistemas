package cap03;
import javax.swing.JOptionPane;


public class questio04 {
	public static void main(String[] args){
		int number = Integer.parseInt(JOptionPane.showInputDialog("Digite um numero: "));
		String complemento = "";
		for(int i =1; i <=10; i++){
			complemento += number+" x "+i+" = "+(number*i)+"\n";
		}
		JOptionPane.showMessageDialog(null, complemento);
	}
}