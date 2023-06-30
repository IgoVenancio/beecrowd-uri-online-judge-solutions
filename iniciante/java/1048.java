package iniciante.java;

import java.io.IOException;
import java.util.*;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);

        double salario = scanner.nextDouble();

        historicoReajuste(salario);
 
    }
    
    static void historicoReajuste(double salario) {
        String[] reajustePorcentagem = {"15 %", "12 %", "10 %", "7 %", "4 %"};
        double[] reajustePercentual = {0.15, 0.12, 0.10, 0.07, 0.04};
        String porcentagemGanho;
        double reajuste;
        double novoSalario;

        if (salario >= 0 && salario <= 400.00) {
            reajuste = reajustePercentual[0] * salario;
            novoSalario = reajuste + salario;
            porcentagemGanho = reajustePorcentagem[0];

        } else if (salario >= 400.01 && salario <= 800.00) {
            reajuste = reajustePercentual[1] * salario;
            novoSalario = reajuste + salario;
            porcentagemGanho = reajustePorcentagem[1];

        } else if (salario >= 800.01 && salario <= 1200.00) {
            reajuste = reajustePercentual[2] * salario;
            novoSalario = reajuste + salario;
            porcentagemGanho = reajustePorcentagem[2];

        } else if (salario >= 1200.01 && salario <= 2000.00) {
            reajuste = reajustePercentual[3] * salario;
            novoSalario = reajuste + salario;
            porcentagemGanho = reajustePorcentagem[3];

        } else {
            reajuste = reajustePercentual[4] * salario;
            novoSalario = reajuste + salario;
            porcentagemGanho = reajustePorcentagem[4];
        }
        System.out.println(String.format("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %s", novoSalario, reajuste, porcentagemGanho));

    }
 
}
