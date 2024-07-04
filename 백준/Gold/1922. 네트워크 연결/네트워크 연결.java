import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        boolean[] visited = new boolean[N];

        List<int[]>[] li = new List[N];
        for(int i = 0; i < N; i++) li[i] = new ArrayList<>();


        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken())-1;
            int to = Integer.parseInt(st.nextToken())-1;
            int cost = Integer.parseInt(st.nextToken());
            li[from].add(new int[]{to, cost});
            li[to].add(new int[]{from, cost});
        }

        int sum = 0, count = 0;     // sum : 비용용도, count : 종료용 간선 갯수 측정용
        int[] w = new int[N];
        for(int i = 0; i < N; i++) w[i] = Integer.MAX_VALUE;

//        for(int i = 0; i < N; i++) {
//            for(int[] k: li[i]) {
//                System.out.print(Arrays.toString(k) + " ");
//            }
//            System.out.println();
//        }

        w[0] = 0;
        for(int i = 0; i < N; i++) {
            int minVertex = -1;
            int min = Integer.MAX_VALUE;
            for(int j = 0; j < N; j++) {
                if(!visited[j] && min > w[j]) {
                    min = w[j];
                    minVertex = j;
                }
            }
            visited[minVertex] = true;
            sum += min;
            if(count++ == N - 1) break;
            for(int[] k: li[minVertex]) {
                if(!visited[k[0]] && w[k[0]] > k[1]) {
                    w[k[0]] = k[1];
                }
            }
        }
        System.out.println(sum);
        br.close();
    }
}
