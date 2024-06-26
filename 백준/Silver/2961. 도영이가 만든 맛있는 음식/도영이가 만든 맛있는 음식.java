import java.util.*;
import java.io.*;

public class Main {

    static int num;
    static int[] sour;
    static int[] bitter;
    static boolean[] visited;
    static int min = Integer.MAX_VALUE;


    static void cook(int cnt, int times, int sum) {
//        if (min < Math.abs(times - sum)) return;        // 이미 최솟값을 넘어서면
        if(cnt == num & sum != 0) {                     // 아무것도 안 넣은 경우 제외
            min = Math.min(min, Math.abs(times - sum));
            return;
        }
        if(cnt == num & sum == 0) {
            return;
        }


        cook(cnt + 1,  times * sour[cnt], sum + bitter[cnt]);
        cook(cnt + 1, times, sum);      // 암것도 안넣을때
    }

    /*static void cook(int cnt) {

        if(cnt == num) {
            int times = 1;
            int sum = 0;
            int count = 0;
            for(int i = 0; i < num; i++) {
                if (visited[i]) {
                    times *= sour[i];
                    sum += bitter[i];
                    count++;
                }

            }
            if (count == 0) return;
            min = Math.min(min, Math.abs(times - sum));
            return ;
        }

        visited[cnt] = true;
        cook(cnt + 1);
        visited[cnt] = false;
        cook(cnt + 1);      // 암것도 안넣을때
    }*/


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        num = Integer.parseInt(br.readLine());
        sour = new int[num];
        bitter = new int[num];
        visited = new boolean[num];

        for(int i = 0; i < num; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            sour[i] = Integer.parseInt(st.nextToken());
            bitter[i] = Integer.parseInt(st.nextToken());
        }

//        cook(0, "");
        cook(0, 1, 0);
        System.out.println(min);
        br.close();
    }
}
