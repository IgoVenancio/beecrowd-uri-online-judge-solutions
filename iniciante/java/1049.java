package iniciante.java;

import java.io.IOException;
import java.util.*;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        
        String palavra1 = scanner.nextLine();
        String palavra2 = scanner.nextLine();
        String palavra3 = scanner.nextLine();

        qualAnimal(palavra1, palavra2, palavra3);
 
    }
    
    static void qualAnimal(String a, String b, String c) {
        String animal;

        if (a.equals("vertebrado")) {
            if (b.equals("ave")) {
                if (c.equals("carnivoro")) {
                    animal = "aguia";
                } else {
                    animal = "pomba";
                }

            } else {
                if (c.equals("onivoro")) {
                    animal = "homem";
                } else {
                    animal = "vaca";
                }
            }

        } else {
            if (b.equals("inseto")) {
                if (c.equals("hematofago")) {
                    animal = "pulga";
                } else {
                    animal = "lagarta";
                }
            } else {
                if (c.equals("hematofago")) {
                    animal = "sanguessuga";
                } else {
                    animal = "minhoca";
                }

            }
        }
        System.out.println(animal);
    }
 
}
