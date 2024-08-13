import java.util.*;

class Solution {
    static int[] p;
    private int find(int a) {
        if(p[a] == a) return a;
        return p[a]=find(p[a]);
    }

    private void union(int a, int b) {
        int ar = find(a);
        int br = find(b);
        if(ar != br) {
            p[br] = ar;
        }
    }
    
    public int solution(int n, int[][] costs) {
        
        Arrays.sort(costs, (o1, o2) -> Integer.compare(o1[2], o2[2]));
        
        p = new int[n];
        for(int i = 0; i < n; i++) p[i] = i;
        int answer = 0;
        for(int[] e : costs) {
            if(find(e[0]) != find(e[1])) {
                union(e[0], e[1]);
                answer += e[2];
            }
        }
        
        return answer;
    }
}