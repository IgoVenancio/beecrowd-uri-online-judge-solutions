import java.io.IOException;
import java.util.*;

 

public class Main {
 
    public static void main(String[] args) throws IOException {
    
        Scanner scanner = new Scanner(System.in);

        int horaInicial = scanner.nextInt();
        int minutoInicial = scanner.nextInt();
        int horaFinal = scanner.nextInt();
        int minutoFinal = scanner.nextInt();

        System.out.println(horaCerta(horaInicial, minutoInicial, horaFinal, minutoFinal));
        
    }
    
    
       static String horaCerta(int a, int b, int c, int d) {

        int horas;
        int minutos;

        if (a == c && b == c && c == d) {
            horas = 24;
            minutos = 0;
            return "O JOGO DUROU " + horas + " HORA(S) E " + minutos + " MINUTO(S)";

        }else if (a == c && b > d) {

            minutos = 60 - b + d;
            horas = 23;

            return "O JOGO DUROU " + horas + " HORA(S) E " + minutos + " MINUTO(S)";

        }else if (a == c && b < d) {
            horas = a - c;
            minutos = d - b;
            return "O JOGO DUROU " + horas + " HORA(S) E " + minutos + " MINUTO(S)";

        } else if (a < c && b == d) {
            horas = c - a;
            minutos = 0;
            return "O JOGO DUROU " + horas + " HORA(S) E " + minutos + " MINUTO(S)";

        } else if (a < c && b < d) {
            horas = c - a;
            minutos = d - b;
            return "O JOGO DUROU " + horas + " HORA(S) E " + minutos + " MINUTO(S)";

        } else if (a > c && b < d) {
            horas = 24 - a + c;
            minutos = d - b;
            return "O JOGO DUROU " + horas + " HORA(S) E " + minutos + " MINUTO(S)";

        } else if (a > c && b > d) {
            horas = 24 - a + c - 1;
            minutos = 60 - b + d;
           
            return "O JOGO DUROU " + horas + " HORA(S) E " + minutos + " MINUTO(S)";

        } else if (a > c && b == d) {
            horas = 24 - a + c;
            minutos = b - d;
            if (minutos == 59){
                horas -= 1;
            }
            return "O JOGO DUROU " + horas + " HORA(S) E " + minutos + " MINUTO(S)";

        }else if (a > c && b > d) {
            horas = 24 - a + c;
            minutos = 60 - b + d;
            return "O JOGO DUROU " + horas + " HORA(S) E " + minutos + " MINUTO(S)";

        } else if (a < c && b > d) {
            horas = c - a - 1;
            minutos = 60 - b + d;
            return "O JOGO DUROU " + horas + " HORA(S) E " + minutos + " MINUTO(S)";
        }else if (a == c && b == d) {
            horas = 24;
            minutos = 0;
            return "O JOGO DUROU " + horas + " HORA(S) E " + minutos + " MINUTO(S)";

        }
        return " ";
    }
 
}
