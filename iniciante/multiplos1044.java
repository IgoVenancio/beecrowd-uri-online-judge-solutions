import java.io.IOException;
import java.util.*;

 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        boolean multiple;
        int number1 = scanner.nextInt();
        int number2 = scanner.nextInt();

        multiple = isMultiple(number1, number2);

        if (multiple){
            System.out.println("Sao Multiplos");
        }else{
            System.out.println("Nao sao Multiplos");
        }
 
    }
    
    static boolean isMultiple(int a, int b){
        int larger = larger(a,b);
        int smaller = smaller(a,b);

        if(larger % smaller == 0){
            return true;
        }else{
            return false;
        }
    }

    static int larger(int a, int b){
        if (a > b){
            return a;
        }else{
            return b;
        }
    }

    static int smaller(int a, int b){
        if (a < b){
            return a;
        }else{
            return b;
        }
    }
 
}
