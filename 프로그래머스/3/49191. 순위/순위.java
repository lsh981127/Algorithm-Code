import java.util.*;
class Solution {
    public int solution(int n, int[][] results) {
        
        int[][] graph = new int[n][n];
        for(int[] i : results) {
            int start = i[0] - 1;
            int end = i[1] - 1;
            graph[start][end] = 1;
            graph[end][start] = -1;
        }
        for(int k = 0; k < n; k++) {
            for(int i = 0; i < n; i++) {
                for(int j = 0; j < n; j++) {
                    if(graph[i][j] != 0) continue;
                    if(graph[i][k] == 1 && graph[k][j] == 1) { // 둘다 1이면 i는 j를 이긴다
                        graph[i][j] = 1;
                    } else if (graph[i][k] == -1 && graph[k][j] == -1) {
                        graph[i][j] = -1;
                    }
                }
            }
        }
        
        int answer = 0;
        
        for(int i[] : graph) {
            int count = 0;
            for(int j : i) {
                if(j == 0) {
                    count++;
                    continue;
                }
            }
            if(count == 1) answer++;
        }
        
        
        return answer;
    }
}