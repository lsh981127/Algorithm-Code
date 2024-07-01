import java.io.*;
import java.util.*;

public class Main {
    static int R, C, K;
    static char[][] arr;
    static boolean[][] visited;
    static int count = 0;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    static void dfs(int x, int y, int tempCount) {

        if(x == 0 && y == C-1) {
            if(tempCount == K) {
                count++;
            }
            return;
        }

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0 <= nx && nx < R && 0 <= ny && ny < C && !visited[nx][ny]) {
                if (arr[nx][ny] != 'T') {
                    visited[x][y] = true;
                    dfs(nx, ny, tempCount+1);
                    visited[x][y] = false;
                }
            }
        }

    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine(), " ");
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        arr = new char[R][C];
        visited = new boolean[R][C];

        for(int i = 0; i < R; i++) {
            char[] temp = br.readLine().toCharArray();
            for(int j = 0; j < C; j++) {
                arr[i][j] = temp[j];
            }
        }

        dfs(R-1, 0, 1);
        System.out.println(count);
    }
}
