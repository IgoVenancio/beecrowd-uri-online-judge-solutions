import java.io.IOException;
import java.util.*;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();
        double delta = Math.pow(b,2) - 4 * a * c;

        if(delta < 0 || a == 0){
            System.out.println("Impossivel calcular");
        }else{
            double r1 = (-b + Math.sqrt(delta))/(2 * a);
            double r2 = (-b - Math.sqrt(delta))/(2 * a);
            System.out.println(String.format("R1 = %.5f\nR2 = %.5f",r1,r2));
        }
 
    }
 
}
