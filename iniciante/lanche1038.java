import java.io.IOException;
import java.util.*;


public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        
        double[] preco = {0.0,4.00,4.50,5.00,2.00,1.50};
        
        int entrada1 = scanner.nextInt();
        int entrada2 = scanner.nextInt();

        System.out.println(String.format("Total: R$ %.2f",preco[entrada1] * entrada2));
 
    }
 
}
