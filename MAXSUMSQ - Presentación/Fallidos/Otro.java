import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Otro {
    private static Integer maximo;
    private static Integer ocurrencias;

    public static void otro(String[]args) throws Exception{
        StringBuilder respuesta = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        Integer casos = Integer.parseInt(br.readLine());

        for(int I=0; I < casos; I++){
            // Integer arr_size = Integer.parseInt(br.readLine());
            br.readLine(); // consumo la linea

            maximo = Integer.MIN_VALUE;
            ocurrencias = 0;

            String[] entrada = br.readLine().split(" ");

            respuesta.append(sumSeq(entrada)).append("\n");
        } 
        
        String rta = respuesta.toString();
        System.out.print(rta);
    }

    private static void comprobar(Integer valor){
        if(valor > maximo){
            maximo = valor;
            ocurrencias = 1;
        }else if(valor == maximo){
            ocurrencias++;
        }
    }

    private static String sumSeq(String[] elems){
        /*
         * def sum_seq(nums):
         *  sumas = [0] * (len(nums))
         *  m = Maximo()
         * 
         *  for I in range(len(nums)):
         *      m.comprobar(nums[I])
         * 
         *      for J in range(I):
         *          sumas[J] += nums[I]
         *          m.comprobar(sumas[J])
         * 
         *      sumas[I] = nums[I]
         * 
         *  return m.get_rta()
         */
        Integer[] nums = Arrays.stream(elems).map(e->Integer.valueOf(e)).toArray(Integer[]::new);
        Integer[] sumas = new Integer[elems.length];
        
        for(int I=0; I<elems.length; I++){
            comprobar(nums[I]);
            for(int J=0; J<I; J++){
                sumas[J] += nums[I];
                comprobar(sumas[J]);
            }
            sumas[I] = nums[I];
        }

        return maximo + " " + ocurrencias;
    }
    
}
