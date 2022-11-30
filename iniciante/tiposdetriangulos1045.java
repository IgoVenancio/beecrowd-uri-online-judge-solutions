import java.io.IOException;
import java.util.*;

 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scanner = new Scanner(System.in);
        float a = scanner.nextFloat();
        float b = scanner.nextFloat();
        float c = scanner.nextFloat();
        float[] entrada = {a,b,c};

        maiorSort(entrada);

        a = entrada[0];
        b = entrada[1];
        c = entrada[2];

        if (naoTriangulo(a, b, c)){
            System.out.println("NAO FORMA TRIANGULO");
        }else{
            if (trianguloRetangulo(a, b, c))
                System.out.println("TRIANGULO RETANGULO");
            if (trianguloObtusangulo(a, b, c))
                System.out.println("TRIANGULO OBTUSANGULO");
            if (trianguloAcutangulo(a, b, c))
                System.out.println("TRIANGULO ACUTANGULO");
            if (trianguloEquilatero(a, b, c))
                System.out.println("TRIANGULO EQUILATERO");
            if (trianguloIsosceles(a, b, c))
                System.out.println("TRIANGULO ISOSCELES");
        }
 
    }
    static boolean naoTriangulo(float a, float b, float c){
        if(a >= (b + c))
            return true;
        return false;
    }

    static boolean trianguloRetangulo(float a, float b, float c){
        if(Math.pow(a,2) == (Math.pow(b,2) + Math.pow(c,2)))
            return true;
        return false;
    }

    static boolean trianguloObtusangulo(float a, float b, float c){
        if(Math.pow(a,2) > (Math.pow(b,2) + Math.pow(c,2)))
            return true;
        return false;
    }

    static boolean trianguloAcutangulo(float a, float b, float c){
        if(Math.pow(a,2) < (Math.pow(b,2) + Math.pow(c,2)))
            return true;
        return false;
    }

    static boolean trianguloEquilatero(float a, float b, float c){
        if(a == b && b == c)
            return true;
        return false;
    }

    static boolean trianguloIsosceles(float a, float b, float c){
        if(a == b && b != c || a == c && c != b || b == c && c != a)
            return true;
        return false;
    }

    static void maiorSort(float[] a){

        for(int i = 0 ; i < a.length - 1; i++){
            for(int j = i + 1 ; j < a.length; j++){
                if(a[i] < a[j]){
                    float aux = a[i];
                    a[i] = a[j];
                    a[j] = aux;
                }
            }
        }
    }
 
}
