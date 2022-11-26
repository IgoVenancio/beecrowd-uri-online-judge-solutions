import java.io.IOException;
import java.util.*;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        String palavra = scanner.nextLine();

        if(palavra.length() >= 10){
            System.out.println("palavrao");
        }else{
            System.out.println("palavrinha");
        }
 
    }
 
}
