package cap02.copy;

import java.util.Scanner;

public class question2 {


	public static void main(String[] args) {
		float lider;
		float lanterna;
		float pontos;
		
		
		Scanner input = new Scanner(System.in);

		System.out.println("Quantidade de pontos do lider:");
		lider = input.nextInt();
		System.out.println("Quantidade de pontos do lanterna:");
		lanterna = input.nextInt();
		pontos = (lider - lanterna) ;
		
		if(pontos % 3 != 0) {
			
			pontos = (pontos / 3) + 1;
			int c1 = (int)pontos;
			
			System.out.println("Quantidade de pontos que o lanterna precisa:" + c1);
		}
		else{
			pontos = (pontos / 3);
			int c1 = (int)pontos;
			System.out.println("Quantidade de pontos que o lanterna precisa:" );
		}
			
			
		
	}

}
