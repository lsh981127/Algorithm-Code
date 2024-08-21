import java.util.*;
class Solution {
    
    public int solution(int m, int n, int[][] puddles) {
        int[][] graph = new int[n+1][m+1];
        int max = 1000000007;
        for(int[] i : puddles) {
            // 와씨... i[1] 과 i[0]을 안바꿔줘서 계속 실패
            
            graph[i[1]][i[0]] = -1;
        }
        
        graph[1][1] = 1;
        // index 처리가 까다로워서 참고
        // 그냥 n+1, m+1로 주고 하면 편한 방법이었어
        for(int i = 1; i < n+1; i++) {
            for(int j = 1; j < m+1; j++) {
                if(graph[i][j] == -1) continue;
                int left = 0, top = 0;
                if(graph[i][j-1] > 0)
                    left = graph[i][j-1] % max;
                if(graph[i-1][j] > 0)
                    top = graph[i-1][j] % max;
                graph[i][j] = (graph[i][j] + left + top) % max;

            }
        }
        
        // for(int[] temp : graph) System.out.println(Arrays.toString(temp));
        
        
        return graph[n][m];
    }
    
    
}