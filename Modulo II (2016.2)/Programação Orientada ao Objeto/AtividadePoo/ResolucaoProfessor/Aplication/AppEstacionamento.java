package Aplication;

import java.util.Arrays;

import javax.swing.JOptionPane;

public class AppEstacionamento {
	public static void main(String[] args){
		String VAGA_LIVRE = "Vaga livre.";
		final String [] vagas = new String[10];
		String menu = "1 - Entrada \n2 - Saida \n3 - Estado\n4 - Sair";
		//Ele inicia o array com um valor default
		Arrays.fill(vagas, VAGA_LIVRE);
		
		while(true){
			
			
			int opcao = Integer.valueOf(JOptionPane.showInputDialog(null, menu));
			
			switch (opcao) {
				case 1://Entrada
					int vaga = Integer.valueOf(JOptionPane.showInputDialog("Vaga: "));
					String placa = JOptionPane.showInputDialog("Placa: ");
					vagas[vaga] = placa;
					
					break;
					
				case 2://Saida
					vaga = Integer.valueOf(JOptionPane.showInputDialog("Vaga: "));
					vagas[vaga] = VAGA_LIVRE;
					JOptionPane.showMessageDialog(null, "Saída ok.");
				case 3://Estado
					String resultado = "Estado: \n";
					for (int i = 0; i < vagas.length; i++) {
						resultado += "Vaga " + i + " -->" + vagas[i] + "\n";
					}
					JOptionPane.showMessageDialog(null, resultado);
					break;

				case 4://Sair
					JOptionPane.showMessageDialog(null, "Até logo!!!!!!");
					return;
					

				default://Opcao Invalida
					JOptionPane.showMessageDialog(null, "Opcao Invalida");
					break;
			
			}
			
			
		}
		
		
	}

}
