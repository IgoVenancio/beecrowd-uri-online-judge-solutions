package iniciante.java;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int A = ler.nextInt();
		int B = ler.nextInt();
		int PROD = A * B;
		
		System.out.println("PROD = "+PROD);
	}

}
