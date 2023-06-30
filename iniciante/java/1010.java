package iniciante.java;

import java.io.IOException;
import java.util.*;
import static java.lang.System.in;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(in);

        String entrada1 = scanner.nextLine();
        String entrada2 = scanner.nextLine();
        String[] textoSeparado1 = entrada1.split(" ");
        String[] textoSeparado2 = entrada2.split(" ");

        double valorPagar1 = (Integer.parseInt(textoSeparado1[1]) * Double.parseDouble(textoSeparado1[2]));
        double valorPagar2 = (Integer.parseInt(textoSeparado2[1]) * Double.parseDouble(textoSeparado2[2]));
        double somaValorPagar = valorPagar1 + valorPagar2;

        System.out.printf("VALOR A PAGAR: R$ %.2f",somaValorPagar);
        skipLine();
 
        
    }
  
    static void skipLine(){
        System.out.println();
    }
  
}
