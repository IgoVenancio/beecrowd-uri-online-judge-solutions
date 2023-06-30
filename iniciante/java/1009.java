package iniciante.java;

import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {

		Scanner entrada = new Scanner(System.in);

		String nome = entrada.nextLine();
		double fixo = entrada.nextDouble();
		double vendas = entrada.nextDouble();
		double salario =  fixo +  0.15 * vendas ;
		
		System.out.printf("TOTAL = R$ %.2f\n",salario);

	}
}
