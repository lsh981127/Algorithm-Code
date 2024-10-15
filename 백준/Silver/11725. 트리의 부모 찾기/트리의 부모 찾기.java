import java.util.*;
import java.io.*;

class Main {
    
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        
        int N = Integer.parseInt(br.readLine());
        boolean[] visited = new boolean[N+1];
        int[] parent = new int[N+1];
        
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < N+1; i++) {
            graph.add(new ArrayList<Integer>());
        }
        for(int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            graph.get(start).add(end);
            graph.get(end).add(start);
        }
        
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        deque.offer(1);
        visited[1] = true;
        while(!deque.isEmpty()) {
            int val = deque.poll();
            ArrayList<Integer> temp = graph.get(val);
            for(int i = 0; i < temp.size(); i++) {
                int cur = temp.get(i);
                if(!visited[cur]) {
                    visited[cur] = true;
                    parent[cur] = val;
                    deque.offer(cur);
                }
            }
        }
        
        for(int i = 2; i < N+1; i++) {
            System.out.println(parent[i]);
        }
        
    }
    
}