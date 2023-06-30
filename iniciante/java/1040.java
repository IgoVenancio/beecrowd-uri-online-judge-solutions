package iniciante.java;

import java.io.IOException;
import java.util.*;
 


public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        float mediaFinal;
        float n1 = scanner.nextFloat();
        float n2 = scanner.nextFloat();
        float n3 = scanner.nextFloat();
        float n4 = scanner.nextFloat();
        float media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1)/10;

        System.out.println(String.format("Media: %.1f",media));
        if(media >= 7.0){
            System.out.println("Aluno aprovado.");
        }else if(media >= 5.0 && media <= 6.9){
            System.out.println("Aluno em exame.");
            float notaExame = scanner.nextFloat();
            System.out.println(String.format("Nota do exame: %.1f",notaExame));
            mediaFinal = (media + notaExame)/2;
            if(mediaFinal>= 5.0){
                System.out.println("Aluno aprovado.");
                System.out.println(String.format("Media final: %.1f",mediaFinal));
            }else{
                System.out.println("Aluno reprovado.");
                System.out.println(String.format("Media final: %.1f",mediaFinal));
            }
        }else{
            System.out.println("Aluno reprovado.");
        }
 
    }
 
}
