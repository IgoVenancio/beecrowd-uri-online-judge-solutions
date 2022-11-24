import java.io.IOException;
import java.util.*;

 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        int mes = 30;
        int ano = 365;

        int idadeDias = scanner.nextInt();
        //anos
        int anos = idadeDias/ano;
        idadeDias -= anos * ano;
        //meses
        int meses = idadeDias/mes;
        //dias
        idadeDias -= meses * mes;

        System.out.println(anos+" ano(s)\n"+meses+" mes(es)\n"+idadeDias+" dia(s)");
 
    }
 
}
