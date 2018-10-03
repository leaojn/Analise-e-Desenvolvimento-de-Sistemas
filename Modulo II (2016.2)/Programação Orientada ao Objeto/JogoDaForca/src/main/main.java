package main;

import java.util.Set;

import aplication.Palavras;

public class main {

	
	public static void main(String[] args) {
		
		Palavras[] arrayPalavras = new Palavras[20];
		Palavras teste = new Palavras();
		teste.setPalavras("ola");
		for (Palavras palavras : arrayPalavras) {
			arrayPalavras[0].setPalavras("Hello");
			System.out.println(arrayPalavras[0]);
		}
		
		
		
		

	}

}
