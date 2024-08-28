import java.util.*;
class Solution {

    public int solution(int[] numbers, int target) {
        
        // numbers 의 숫자 순서는 변하지 않는다.
        // 모든 숫자 앞에 + 일지, -일지만 고려하기
        // 각 값들은 양수, 즉 -1을 곱할지 말지만 고려하면 된다.
        int size = numbers.length;
        boolean[] visited = new boolean[size];  
        int[] dir = new int[]{1, -1};
        ArrayDeque<int[]> aq = new ArrayDeque<>();
        aq.offer(new int[]{0, 0});
        // 왼쪽이 몇번째 숫자 작업중인지, 오른쪽이 숫자
        int answer = 0;
        while(!aq.isEmpty()) {
            int[] temp = aq.poll();
            int cur = temp[0];
            int num = temp[1];
            if(cur == size) {
                if(num == target) {
                    answer++;
                }
                continue;
            }
            
            if(cur < size) {
                int val = numbers[cur];
                for(int i : dir) {
                    int count = num + val * i;
                    aq.offer(new int[]{cur+1, count});
                }
            }
        }
        return answer;
    }

    
}