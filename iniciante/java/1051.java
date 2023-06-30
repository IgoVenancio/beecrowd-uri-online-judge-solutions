package iniciante.java;

import java.io.IOException;
import java.util.*;


public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        double salario = scanner.nextDouble();

        imprimirImpostoDeRenda(salario);
 
    }
    
    static void imprimirImpostoDeRenda(double a){
        double imposto;

        if (a >= 0.00 && a <= 2000.00){
            System.out.println("Isento");
        }else if (a >= 2000.01 && a <= 3000.00){
            imposto = (a - 2000.00) * 0.08;
            System.out.println(String.format("R$ %.2f",imposto));
        } else if (a >= 3000.01 && a <= 4500.00) {
            imposto = (a - 3000.00) * 0.18 + (3000.00 - 2000.00) * 0.08;
            System.out.println(String.format("R$ %.2f",imposto));
        }else{
            imposto = (a - 4500.00) * 0.28 + (4500 - 3000) * 0.18 + (3000.00 - 2000.00) * 0.08;
            System.out.println(String.format("R$ %.2f",imposto));
        }
    }
 
}
