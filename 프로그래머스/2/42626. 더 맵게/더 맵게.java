import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i : scoville) {
            pq.offer(i);
        }
        
        int answer = 0;
        while(true) {
            int temp = pq.poll();
            if(temp >= K)
                return answer;
            if(pq.isEmpty())
                break;
            int mix = temp + pq.poll() * 2;
            answer++;
            pq.offer(mix);
        }
        return -1;
    }
}