package iniciante.java;

import java.io.IOException;
import java.util.*;
import static java.lang.System.*;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
        double pi = 3.14159;
        Scanner scanner = new Scanner(in);
        double radius = scanner.nextDouble();
        double area = pi * Math.pow(radius,2);
        System.out.printf("A=%.4f",area);
        skipLine();
    }
    static void skipLine(){
        System.out.println();
    }
 
}
