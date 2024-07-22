import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int current = 0;
        int total = 0;
        int count = 0;
        int index = 0;


        Arrays.sort(jobs, (o1,o2) -> o1[0] - o2[0]);

        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[1] - b[1]);
        while(count < jobs.length) {
            while (index < jobs.length && current >= jobs[index][0]) {
                pq.offer(jobs[index++]);
            }

            if(pq.isEmpty()) {
                current = jobs[index][0];  // 다음 작업의 시작점으로 current 옮기기
            } else {
                // pq에 값들 남아 있는 경우
                int[] temp = pq.poll();
                total += current + temp[1] - temp[0];
                count++;
                current += temp[1];
            }

        }

        int answer = total / jobs.length;
        return answer;
    }
}