import java.io.IOException;
import java.util.*;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);

        float n1 = scanner.nextFloat();
        float n2 = scanner.nextFloat();

        if(n1 > 0 && n2 > 0){
            System.out.println("Q1");
        } else if (n2 > 0 && n1 < 0) {
            System.out.println("Q2");
        } else if (n1 < 0 && n2 < 0) {
            System.out.println("Q3");
        } else if (n1 > 0 && n2 < 0) {
            System.out.println("Q4");
        } else if (n1 == 0 && n2 != 0) {
            System.out.println("Eixo Y");
        } else if (n1 != 0 && n2 == 0) {
            System.out.println("Eixo X");
        }else if (n1 == 0 && n2 == 0){
            System.out.println("Origem");
        }
 
    }
 
}
