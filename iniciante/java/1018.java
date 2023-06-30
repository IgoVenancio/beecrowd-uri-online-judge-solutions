package iniciante.java;

import java.io.IOException;
import java.util.*;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
            Scanner scanner = new Scanner(System.in);

            int valor = scanner.nextInt();
            int resultado;
            
            System.out.println(valor);

            //100
            resultado = valor/100;
            System.out.println(resultado +" nota(s) de R$ 100,00");
            valor = valor - (resultado * 100);

            //50
            resultado  = valor/50;
            System.out.println(resultado +" nota(s) de R$ 50,00");
            valor = valor - (resultado * 50);

            //20
            resultado = valor/20;
            System.out.println(resultado+" nota(s) de R$ 20,00");
            valor = valor - (resultado * 20);

            //10
            resultado = valor/10;
            System.out.println(resultado+" nota(s) de R$ 10,00");
            valor = valor - (resultado * 10);

            //5
            resultado = valor/5;
            System.out.println(resultado+" nota(s) de R$ 5,00");
            valor = valor - (resultado * 5);

            //2
            resultado = valor/2;
            System.out.println(resultado+" nota(s) de R$ 2,00");
            valor = valor - (resultado * 2);

            //1
            resultado = valor/1;
            System.out.println(resultado+" nota(s) de R$ 1,00");
 
    }
 
}
