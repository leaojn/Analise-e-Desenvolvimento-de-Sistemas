package cap02;


import java.io.*;
public class DescontoProduto {


		public static void main(String[] args) {
			
			String s;
			float percentual, produto, desconto, perimetro;
			BufferedReader dado;
			
			
			try {
				
				System.out.println("Digite o valor do produto:");
				dado = new BufferedReader(new InputStreamReader(System.in));
				s = dado.readLine();
				produto = Float.parseFloat(s);
				
				System.out.println("Digite a porcentagem do desconto");
				dado = new BufferedReader(new InputStreamReader(System.in));
				s = dado.readLine();
				percentual = Float.parseFloat(s);
				
				desconto = produto * percentual / 100;
				
				System.out.println("Valor do produto com desconto:" + (produto - desconto));
				System.out.println("Valor do desconto:" + desconto);
				
			
			
			}
			catch (IOException erro){
				System.out.println("Houve um erro na entrada de dados" + erro.toString());
			}
			catch (NumberFormatException erro){
				
				System.out.println("Houve um erro na conversao, digite apenas caracteres numericos" + erro.toString());
				
				
			}
		}

	}
