import java.io.IOException;
import java.util.*;

 

public class Main {
 
    public static void main(String[] args) throws IOException {
    
        Scanner scanner = new Scanner(System.in);
        int ddd = scanner.nextInt();

        System.out.println(dddCidade(ddd));
 
    }
    
    static String dddCidade(int value){
        String cidade = switch(value){
            case 61 -> "Brasilia";
            case 71 -> "Salvador";
            case 11 -> "Sao Paulo";
            case 21 -> "Rio de Janeiro";
            case 32 -> "Juiz de Fora";
            case 19 -> "Campinas";
            case 27 -> "Vitoria";
            case 31 -> "Belo Horizonte";
            default -> "DDD nao cadastrado";
        };

        return cidade;
    }
    
 
}
