import java.util.*;
class Solution {
    
    static boolean[] visited;
    static List<String> path;
    public static String[] solution(String[][] tickets) {
        visited = new boolean[tickets.length];
        path = new ArrayList<>();
        int count = 0;

        dfs(count, "ICN", "ICN", tickets);
        Collections.sort(path);
        String[] answer = path.get(0).split(" ");

        return answer;
    }

    static void dfs(int count, String current, String way, String [][] tickets) {
        if(count == tickets.length) {
            path.add(way);
            return;
        }

        for(int i = 0; i < tickets.length; i++) {
            if(!visited[i] && current.equals(tickets[i][0])) {
                visited[i] = true;
                dfs(count + 1, tickets[i][1],  way + " " + tickets[i][1], tickets);
                visited[i] = false;

            }
        }
    }
    
}