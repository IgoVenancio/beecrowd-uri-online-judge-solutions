package iniciante.java;

import java.io.IOException;
import java.util.*;


public class Main {
 
    public static void main(String[] args) throws IOException {
 
            Scanner scanner = new Scanner(System.in);
            int consumoPorLitro = 12;

            int tempo = scanner.nextInt();;
            int velocidadeMedia = scanner.nextInt();

            double litros = (double)(tempo * velocidadeMedia) /consumoPorLitro;

            System.out.println(String.format("%.3f",litros));
 
    
    }

    
}
