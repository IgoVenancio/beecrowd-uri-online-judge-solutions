import java.io.IOException;
import java.util.*;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
            Scanner scanner = new Scanner(System.in);

            String entrada = scanner.nextLine();
            String[] entradas = entrada.split(" ");

            double a = Double.parseDouble(entradas[0]);
            double b = Double.parseDouble(entradas[1]);
            double c = Double.parseDouble(entradas[2]);
            double pi = 3.14159;

            System.out.printf("TRIANGULO: %.3f",(a * c)/2);
            skipLine();
            System.out.printf("CIRCULO: %.3f",(pi * Math.pow(c,2)));
            skipLine();
            System.out.printf("TRAPEZIO: %.3f",((a + b) * c)/2);
            skipLine();
            System.out.printf("QUADRADO: %.3f",Math.pow(b,2));
            skipLine();
            System.out.printf("RETANGULO: %.3f",(a * b));
            skipLine();
 
    }
    static void skipLine(){
        System.out.println();
    }
 
}
