import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    static final int[] dx = {-1, 0, 1, 0};
    static final int[] dy = {0, 1, 0, -1};

    static int N;
    static int[][] arr;
    static boolean[][] visited;

    static void dfs(int x, int y, int avg) {
        visited[x][y] = true;
        for(int d =0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            if(nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
                if(arr[nx][ny] > avg) {     // 잠기는 높이보다 큰 경우만 고려
                    dfs(nx,ny, avg);
                }

            }
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];

        int max_height = 0;
        int answer = 0;
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int temp = Integer.parseInt(st.nextToken());
                max_height = Math.max(max_height,temp);
                arr[i][j] = temp;
            }
        }

        for(int h = 0; h < max_height; h++) {
            // 새 높이에 대해 초기화
            visited = new boolean[N][N];
            int temp_answer = 0;
            for(int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if(arr[i][j] > h && !visited[i][j]) {
                        dfs(i, j, h);
                        temp_answer++;
                    }
                }
            }
            answer = Math.max(answer, temp_answer);
        }

        System.out.println(answer);


    }
}
