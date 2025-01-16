import java.util.*;
import java.io.*;
public class Main {
    static char[][] graph;
    static HashSet<Integer> set = new HashSet<>();
    static int result = 0;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int R, C;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        graph = new char[R][C];
        for(int i = 0; i < R; i++) {
            char[] temp = br.readLine().toCharArray();
            for(int j = 0; j < C; j++) {
                graph[i][j] = temp[j];
            }
        }

        set.add(graph[0][0] - 'A');
        dfs(0, 0, 1);
        System.out.println(result);
    }

    static void dfs(int x, int y, int count) {
        set.add(graph[x][y] - 'A');
        result = Math.max(result, count);
        for(int i = 0; i < 4; i++) {
            int tx = x + dx[i];
            int ty = y + dy[i];
            if(tx >= 0 && tx < R && ty >= 0 && ty < C) {
                int val = graph[tx][ty] - 'A';
                if(!set.contains(val)) {
                    dfs(tx, ty, count + 1);
                    set.remove(val);
                }
            }
        }
    }

}
