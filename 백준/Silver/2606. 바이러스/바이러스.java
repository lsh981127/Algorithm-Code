import java.util.*;
import java.io.*;
public class Main {
    static int N, M;
    static List<Integer>[] network;      // 네트워크  
    static boolean[] visited;   
    static int total;    // DFS에서 사용하는 감염된 바이러스 갯수                
    
    static int bfs(int k) {
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.offer(k);
        visited[k] = true;
        
        // 매 bfs를 돌릴때마다 감염되는 컴퓨터의 갯수를 구하기 위해 초기화
        int bfsTemp = 0;
        
        while (!q.isEmpty()) {
            int i = q.poll();
            for(int j : network[i]) {
                if(!visited[j]) {
                    visited[j] = true;
                    bfsTemp++;            // 감염되기에 갯수 1 증가
                    q.offer(j);
                }
            }
        }
        return bfsTemp;                    // 해당 바이러스로 인해 전염된 갯수 return
    }

    static void dfs(int k) {
        visited[k] = true;
        for(int j: network[k]) {
            if(!visited[j]) {;
                total++;                // 감염된 컴퓨터 증가
                dfs(j);
            }
        }
    }


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        
        // 인접리스트 초기화
        network = new List[N];
        for(int i =0; i < N; i++) network[i] = new ArrayList<>();
        
        visited = new boolean[N];
        
        // DFS용 바이러스 갯수 화긴
        total = 0;
        for(int i =0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            network[from-1].add(to-1);
            network[to-1].add(from-1);
        }
        
        // DFS 실행
        dfs(0);
        System.out.println(total);
        
        // BFS 실행
        // System.out.println(bfs(0));
    }
}
