package Utils;
import java.io.IOException;
import java.util.Scanner;
import java.util.*;



public class IOTools {
	
	public static String getString(String mensagem) {
		
		System.out.println(mensagem);
		Scanner sc;
		sc = new Scanner(System.in);
		return sc.next();
	}
	
	public static int getInt(String mensagem){
	try{
		System.out.println(mensagem);
		Scanner sc;
		sc = new Scanner(System.in);
		return sc.nextInt();
			
	} catch(InputMismatchException e){
		System.out.println("Houve um erro!!\ndigite apenas caracteres numericos ");
	}
	return getInt( mensagem);
	}
		
	
	public static double getReal(String mensagem){
		try{
		System.out.println(mensagem);
		Scanner sc;
		sc = new Scanner(System.in);
		return  sc.nextFloat();
	} catch(InputMismatchException e){
		System.out.println("Houve um erro!!\nDigite apenas caracteres numericos ");
		return getInt( mensagem);
	}
	
	}
		
		
	
		
	public static void showMessage(String mensagem){
		
		System.out.println(mensagem);
			
	}

	

}