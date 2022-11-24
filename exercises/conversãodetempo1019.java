import java.io.IOException;
import java.util.*;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
       Scanner scanner = new Scanner(System.in);

        int segundos= scanner.nextInt();

        //horas
        int horas = segundos/3600;
        segundos -= horas * 3600;
        //minutos
        int minutos = segundos/60;
        //segundos
        segundos -= minutos * 60;

        System.out.println(horas+":"+minutos+":"+segundos);
 
    }
 
}
