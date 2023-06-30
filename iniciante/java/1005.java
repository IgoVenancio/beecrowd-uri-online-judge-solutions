package iniciante.java;

import java.util.Scanner;

public class Main {

	public static void main(String[] args)  {
		
		Scanner ler = new Scanner(System.in);
		
		double A = ler.nextDouble();
		double B = ler.nextDouble();
		double MEDIA =(double) ((3.5)*A + (7.5)*B)/11;
		
		System.out.printf("MEDIA = %.5f\n",MEDIA);
    
	}

}
