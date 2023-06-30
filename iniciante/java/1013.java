package iniciante.java;

import java.io.IOException;
import java.util.*;


public class Main {
 
    public static void main(String[] args) throws IOException {
 
         Scanner scanner = new Scanner(System.in);

            String entrada = scanner.nextLine();
            String[] entradas = entrada.split(" ");

            int a = Integer.parseInt(entradas[0]);
            int b = Integer.parseInt(entradas[1]);
            int c = Integer.parseInt(entradas[2]);
            int maior = maior(a, b, c);

            System.out.println(maior+" eh o maior");
 
    }
    static int maior(int a, int b, int c){
        int maior = (a + b + Math.abs(a - b))/2;
        return (maior + c + Math.abs(maior - c))/2;
    }
 
}
