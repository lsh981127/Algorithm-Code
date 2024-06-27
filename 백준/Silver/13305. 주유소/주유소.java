import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int num = Integer.parseInt(br.readLine());
        int[] distance = new int[num-1];    //
        int[] city = new int[num-1];          // 근데 마지막 어차피 안쓰지 않나?

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < num-1; i++) {
            distance[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < num-1; i++) {
            city[i] = Integer.parseInt(st.nextToken());
        }


        int min = city[0];
        int total = distance[0] * min;

        for(int i = 1; i < num-1; i++) {
            if (min > city[i]) {
                min = city[i];
            }
            total += distance[i] * min;
        }

        System.out.println(total);


    }
}
