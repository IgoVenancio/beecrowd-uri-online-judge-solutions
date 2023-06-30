package iniciante.java;

import java.io.IOException;
import java.util.*;

 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        int horaInicial = scanner.nextInt();
        int horaFinal = scanner.nextInt();

        System.out.println(String.format("O JOGO DUROU %d HORA(S)",duracaoJogo(horaInicial, horaFinal)));
 
    }
    
    static int duracaoJogo(int a, int b){
        if (a == b)
            return 24;
        if (a > b)
            return 24 - a + b;
        if (a < b)
            return b - a;
        return -1;
    }
 
}
