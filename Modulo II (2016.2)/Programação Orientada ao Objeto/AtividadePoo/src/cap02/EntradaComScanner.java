package cap02;


import java.util.*;

public class EntradaComScanner {

	
public static void main(String[] args) {
		
		float largura, comprimento, area, perimetro;
		Scanner sc;
		
		
		try {
			
			System.out.println("Entre com o comprimento:");
			sc = new Scanner(System.in);
			comprimento = sc.nextFloat();
			
			
			System.out.println("Entre com a largura:");
			sc = new Scanner(System.in);
			largura = sc.nextFloat();
			
			area = comprimento * largura;
			perimetro = comprimento * 2 + largura * 2;
			System.out.println("Área do retangulo:" + area);
			System.out.println("Perimetro do retangulo:" + perimetro);
			
		
		
		}
		
		catch (NumberFormatException erro){
			
			System.out.println("Houve um erro na conversao, digite apenas caracteres numericos" + erro.toString());
			
			
		}
	}

}
