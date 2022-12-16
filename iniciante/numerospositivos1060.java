import java.io.IOException;
import java.util.*;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        int contador1 = 0;
        int contador2 = 0;

        while (contador1 < 6){
            double entrada = scanner.nextDouble();

            if (entrada > 0)
                contador2++;
            if (entrada != 0)
                contador1++;

        }

        System.out.println(String.format("%d valores positivos", contador2));
 
    }
 
}
