import java.util.*;

class Solution {
    static boolean[] visited;
    static int max;
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        dfs(dungeons, k, 0);
        return max;
    }
    
    static void dfs(int[][] dungeons, int current, int count) {  
        
        for(int i = 0; i < dungeons.length; i++) {
            if(visited[i] || dungeons[i][0] > current) {    
                continue;
            }
            visited[i] = true;
            dfs(dungeons, current - dungeons[i][1], count + 1);
            visited[i] = false;
        }
        
        max = Math.max(max, count);
        
        
    }
}