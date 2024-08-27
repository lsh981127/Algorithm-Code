import java.util.*;
class Solution {
    static boolean[] v;
    static int answer = 0;
    static int size;
    static int[][] comp;
    public static int solution(int n, int[][] computers) {
        
        // 각 노드들의 시작점에 대해 DFS 돌려서 연결된 네트워크 탐색
        comp = new int[n][n];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                comp[i][j] = computers[i][j];
            }
        }        
        v = new boolean[n];
        size = n;
        
        for(int i = 0; i < n; i++) {
            if(v[i]) continue;
            answer++;
            dfs(i);
        }
        
        return answer;
    }
    
    static void dfs(int x) {
        for(int i = 0; i < size; i++) {
            if(i == x || comp[x][i] != 1 || v[i])
                continue;
            v[i] = true;
            dfs(i);
        }
    }
}