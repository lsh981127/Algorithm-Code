import java.util.*;
import java.io.*;

public class Main {
    static int[] num = new int[9];
    static int[] arr = new int[7];

    static void comb(int count, int start, int sum){
        if (count == 7) {
            if (sum == 100){
                for(int i = 0; i < arr.length;i++)
                    System.out.println(arr[i]);
            }
            return;
        }

        for (int i = start; i < num.length; i++) {
            arr[count] = num[i];
            comb(count+1, i+1, sum + num[i]);
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int i = 0; i < num.length; i++) {
            num[i] = Integer.parseInt(br.readLine());
        }

        comb(0,0, 0);

        br.close();
    }
}
