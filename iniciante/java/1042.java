package iniciante.java;

import java.io.IOException;
import java.util.*;


public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);

        int number1 = scanner.nextInt();
        int number2 = scanner.nextInt();
        int number3 = scanner.nextInt();
        int[] entrada = {number1,number2, number3};
        int[] entrada1 = {number1,number2, number3};

        sort(entrada);

        printArray(entrada);

        skipLine();

        printArray(entrada1);
 
    }
    static void sort(int[] array1){
        for(int i = 0 ; i < array1.length - 1; i++){
            for(int j = i + 1; j < array1.length; j++){
                if(array1[j] < array1[i]){
                    int aux = array1[i];
                    array1[i] = array1[j];
                    array1[j] = aux;
                }
            }
        }
    }

    static void printArray(int [] array){
        for(int x : array){
            System.out.println(x);
        }
    }

    static void skipLine(){
        System.out.println();
    }
 
}
