import java.io.IOException;
import java.util.*;


public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        float a = scanner.nextFloat();
        float b = scanner.nextFloat();
        float c = scanner.nextFloat();

        if((Math.abs(b-c) < a && a < (b + c)) || (Math.abs(a-c) < b && b < (a + c)) || (Math.abs(a-b) < c && c < (a + b))){
            float perimetro = a + b + c;
            System.out.println(String.format("Perimetro = %.1f",perimetro));

        }else{
            float area = ((a + b) * c)/2;
            System.out.println(String.format("Area = %.1f",area));
        }
 
    }
 
}
