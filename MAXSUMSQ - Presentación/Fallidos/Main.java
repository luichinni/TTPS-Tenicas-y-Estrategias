import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main{
    
    private static Integer maximo;
    private static Integer ocurrencias;
    
    public static void main(String[] args) throws Exception {
        /*
        Input es
        1. num T de cantidad de casos
        2. cantidad n nros en primer array
        3. array separado por espacios con cada Ai
        <-> se repite hasta 2*T lineas <->

        Donde:
        1 <= T <= 35 (max 35 casos)
        1 <= n <= 100000 (max 100k numeros por array)
        -1000 <= Ai <= 1000 (los nros del array van desde -10k hasta 10k)

        Output:
        Por cada caso imprimir separado por espacios, el nro maximo sumado consecutivo y la cantidad de veces
        que aparece

        nro_maximo_sumado cant_veces_calculado
        */

        StringBuilder respuesta = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        Integer casos = Integer.parseInt(br.readLine());

        for(int I=0; I < casos; I++){
            // Integer arr_size = Integer.parseInt(br.readLine());
            br.readLine(); // consumo la linea

            maximo = Integer.MIN_VALUE;
            ocurrencias = 0;

            Integer[] entrada = Arrays.stream(br.readLine().split(" "))
                                        .map(elem -> Integer.valueOf(elem))
                                        .toArray(Integer[]::new);

            Integer[] RSQ = prepararRSQ(entrada);

            respuesta.append(procesarRSQ(RSQ)).append("\n");
        } 
        
        String rta = respuesta.toString();
        System.out.print(rta);
    }
    
    public static String procesarRSQ(Integer[] nros){
        /*
        * def max_sum_sq(nros):
        *  m = Maximo()
        * 
        *  for L in range(1,len(nros)):
        *      for R in range(L,len(nros)):
        *          valor = nros[R] - nros[L-1]
        *          m.comprobar(valor)
        * 
        *  return m.get_rta()
        */
        for(int L=1; L < nros.length; L++){
            for(int R=L; R < nros.length; R++){
                if(nros[R]-nros[L-1] > maximo){
                    maximo = nros[R]-nros[L-1];
                    ocurrencias = 0;
                }else if(nros[R]-nros[L-1] == maximo){
                    ocurrencias++;
                }
            }
        }
        return maximo + " " + ocurrencias;
    }

    public static Integer[] prepararRSQ(Integer[] nums){
        /*
         * def preparar_rsq(nums):
         *  numeros = [0] * (len(nums)+1)
         * 
         *  for I in range(1,len(numeros)):
         *  numeros[I] = nums[I-1] + numeros[I-1]
         * 
         *  return numeros
         */
        Integer[] numeros = new Integer[nums.length+1];
        numeros[0] = 0;

        for(int I=1; I < numeros.length; I++){
            numeros[I] = nums[I-1] + numeros[I-1];
        }

        return numeros;
    }
}