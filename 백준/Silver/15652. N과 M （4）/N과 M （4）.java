import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] num;
    static int[] arr;

    static void comb(int count, int start) {
        if(count == M) {
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < M; i++) {
                sb.append(arr[i]).append(" ");
            }
            System.out.println(sb);
            return ;
        }

        for(int i = start; i < N; i++) {
            arr[count] = num[i];
            comb(count + 1, i);
        }

    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        num = new int[N];
        arr = new int[M];
        for(int i = 0; i < N; i++) {
            num[i] = i+1;
        }
        comb(0, 0);


    }
}
