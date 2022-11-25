import java.io.IOException;
import java.util.*;


public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        double valorMonetario = scanner.nextDouble();
        int qtdNotas, entrou = 0;
        double qtdMoedas1, qtdMoedas50, qtdMoedas25, qtdMoedas10, qtdMoedas5, qtdMoedas01;
        qtdMoedas1 = qtdMoedas50 = qtdMoedas25 = qtdMoedas10 = qtdMoedas5 = qtdMoedas01 = 0.0;


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


        System.out.println("MOEDAS:");

        //1
        if (valorMonetario >= 1.00) {
            qtdMoedas1 = (int) valorMonetario / 1.00;
            valorMonetario %= 1.00;
        }
        //0.50
        if (valorMonetario >= 0.50) {
            qtdMoedas50 = valorMonetario / 0.50;
            qtdMoedas50 = (int)qtdMoedas50;
            valorMonetario %= 0.50;
        }
        //0.25
        if (valorMonetario >= 0.25) {
            qtdMoedas25 = valorMonetario / 0.25;
            qtdMoedas25 = (int)qtdMoedas25;
            valorMonetario %= 0.25;

        }
        //0.10
        if (valorMonetario >= 0.10) {
            qtdMoedas10 =  valorMonetario / 0.10;
            qtdMoedas10 = (int)qtdMoedas10;
            valorMonetario %= 0.10;
        }
        //0.05
        if (valorMonetario >= 0.05) {
            qtdMoedas5 = valorMonetario / 0.05;
            qtdMoedas5 = (int)qtdMoedas5;
            valorMonetario %= 0.05;
        }
        //0.01
        if (valorMonetario >= 0.01) {
            qtdMoedas01 = valorMonetario / 0.01;
            entrou++;
        }
      
        if(valorMonetario != 0 && entrou == 0){
            qtdMoedas01++;
        }

        System.out.println(String.format("%.0f moeda(s) de R$ 1.00", qtdMoedas1));
        System.out.println(String.format("%.0f moeda(s) de R$ 0.50", qtdMoedas50));
        System.out.println(String.format("%.0f moeda(s) de R$ 0.25", qtdMoedas25));
        System.out.println(String.format("%.0f moeda(s) de R$ 0.10", qtdMoedas10));
        System.out.println(String.format("%.0f moeda(s) de R$ 0.05", qtdMoedas5));
        System.out.println(String.format("%.0f moeda(s) de R$ 0.01", qtdMoedas01));
 
    }
 
}
