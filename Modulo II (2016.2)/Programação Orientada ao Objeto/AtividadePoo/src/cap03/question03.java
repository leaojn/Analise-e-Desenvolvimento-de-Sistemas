package cap03;
import javax.swing.*;


public class question03 {
	public static void main(String[] args){
		final String lg = "java8";
		int contador = 3;
	
		while (contador > -1){
			String login = JOptionPane.showInputDialog(null, "Digite o login:");
			String senha = JOptionPane.showInputDialog(null, "Digite a senha:");
			
			
			if (lg.equals(login) && lg.equals(login)){
				JOptionPane.showMessageDialog(null, "Login e Senha aceitos!");
				break;
			}
			else{
				JOptionPane.showMessageDialog(null, "Falha no Login "+"\n" + "verifique login e senha" +"\n"+ "voce tem mais "+contador+" tentativas");
					contador-=1;
			}
		}
		
	}

}