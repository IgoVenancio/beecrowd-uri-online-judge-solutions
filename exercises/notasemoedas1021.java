mport java.io.IOException;
import java.util.*;


public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        double valorMonetario = Double.parseDouble(scanner.nextLine());
        int qtdNotas;
        int qtdMoedas;

        System.out.println("NOTAS:");

        //100
        qtdNotas = (int) valorMonetario / 100;
        valorMonetario %= 100;
        System.out.println(qtdNotas + " nota(s) de R$ 100.00");
        //50
        qtdNotas = (int) valorMonetario / 50;
        valorMonetario %= 50;
        System.out.println(qtdNotas + " nota(s) de R$ 50.00");
        //20
        qtdNotas = (int) valorMonetario / 20;
        valorMonetario %= 20;
        System.out.println(qtdNotas + " nota(s) de R$ 20.00");
        //10
        qtdNotas = (int) valorMonetario / 10;
        valorMonetario %= 10;
        System.out.println(qtdNotas + " nota(s) de R$ 10.00");
        //5
        qtdNotas = (int) valorMonetario / 5;
        valorMonetario %= 5;
        System.out.println(qtdNotas + " nota(s) de R$ 5.00");
        //2
        qtdNotas = (int) valorMonetario / 2;
        valorMonetario %= 2;
        System.out.println(qtdNotas + " nota(s) de R$ 2.00");

        //Multiplicar por 100 para diminuir os erros de precições
        System.out.println("MOEDAS:");
        valorMonetario *= 100.00;
        //1
        qtdMoedas =  (int)valorMonetario / 100;
        valorMonetario %= 100;
        System.out.println(qtdMoedas + " moeda(s) de R$ 1.00");

        //0.50
        qtdMoedas =  (int)valorMonetario / 50;
        valorMonetario %= 50;
        System.out.println(qtdMoedas + " moeda(s) de R$ 0.50");

        //0.25
        qtdMoedas =  (int)valorMonetario / 25;
        valorMonetario %= 25;
        System.out.println(qtdMoedas + " moeda(s) de R$ 0.25");

        //0.10
        qtdMoedas =  (int)valorMonetario / 10;
        valorMonetario %= 10;
        System.out.println(qtdMoedas + " moeda(s) de R$ 0.10");

        //0.05
        qtdMoedas =  (int)valorMonetario / 5;
        valorMonetario %= 5;
        System.out.println(qtdMoedas + " moeda(s) de R$ 0.05");

        //0.01
        qtdMoedas =  (int)valorMonetario / 1;
        valorMonetario %= 1;
        if(Math.round(valorMonetario) == 1){
            qtdMoedas +=1;
        }
        System.out.println(qtdMoedas + " moeda(s) de R$ 0.01");
 
    }
 
}
