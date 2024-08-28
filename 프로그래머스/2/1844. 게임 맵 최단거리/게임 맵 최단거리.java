import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        ArrayDeque<int[]> dq = new ArrayDeque<>();
        int n = maps.length;
        int m = maps[0].length;
        boolean[][] v = new boolean[n][m];
        int[] dx = new int[]{1, 0, -1, 0};
        int[] dy = new int[]{0, 1, 0, -1};

        v[0][0] = true;
        dq.offer(new int[]{0,0});
        while(!dq.isEmpty()) {
            int[] temp = dq.poll();
            int x = temp[0];
            int y = temp[1];

            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(0 <= nx && nx < n && 0 <= ny && ny < m && !v[nx][ny]) {
                    // 난 누적값으로 저장할 것이기에 1인 경우만 진행하면 된다.
                    // 0이면 막힌 거, 1이 아닌 양수면 이미 누가 방문한 거
                    if(maps[nx][ny] == 1) {
                        maps[nx][ny] += maps[x][y];
                        v[nx][ny] = true;
                        dq.offer(new int[]{nx,ny});
                    }
                }
            }
        }
        
        if(maps[n-1][m-1] != 1) {
            return maps[n-1][m-1];
        }
        return -1;
        
        
    }
}