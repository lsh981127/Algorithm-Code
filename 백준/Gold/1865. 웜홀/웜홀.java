import java.util.*;
import java.io.*;
class World {
    int start;
    int end;
    int cost;

    World(int start, int end, int cost) {
        this.start = start;
        this.end = end;
        this.cost = cost;
    }
}

public class Main {

    static ArrayList<World> graph;
    static final int MAX = 100000000;
    static int[] dist;
    static BufferedReader br;
    public static void main(String[] args) throws Exception{
        br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        for(int i = 0; i < TC; i++) {
            testcase();
        }

    }

    public static void testcase() throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        for(int i = 0; i < M; i++) {
            st  = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            graph.add(new World(start, end, cost));
            graph.add(new World(end, start, cost));
        }

        for(int i = 0; i < W; i++) {
            st  = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            graph.add(new World(start, end, cost * -1));
        }

        // 간선의 갯수가 2M + W다. 계속 M + W로 진행하고 있었네
        if(BellmanFord(N)) System.out.println("YES");
        else System.out.println("NO");
    }


    public static boolean BellmanFord(int n) {
        dist = new int[n+1];

        // 특정 점에서 모든 정점으로 가는 최단 거리를 구할 때에는 최대값으로 해야함
//        Arrays.fill(dist, MAX);
        // 그러나, 음수 사이클 탐지용에서는 모든 정점을 대상으로 조사해야하므로 0으로 초기화해야

        // N-1번 탐색
        for(int i = 0; i < n-1; i++) {
            boolean updated = false;
            for(World world : graph) {
                if(dist[world.end] > dist[world.start] + world.cost) {
                    dist[world.end] = dist[world.start] + world.cost;
                    updated = true;
                }
            }
            if(!updated) break;
        }

        // 위에서 N번 반복했으니 이번에 1번만 더 진행해서(모든 간선에 대한 탐색)
        for(World world : graph) {
            if(dist[world.end] > dist[world.start] + world.cost) {
                return true;
            }
        }
        return false;
    }


}
