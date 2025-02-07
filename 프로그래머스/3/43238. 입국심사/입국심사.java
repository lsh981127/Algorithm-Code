import java.util.*;
class Solution {
    
    public long solution(int n, int[] times) {
        Arrays.sort(times);  // 혹시 모르니 시간 정렬
        long start = 0;
        long end = times[times.length - 1] * (long) n;  // 제일 빨리 끝나는 애한테 모든 애들이 검사받는 경우를 최대로 가정
        long answer = 0;
        while(start <= end) {
            long mid = (start + end) / 2;
            long count = 0;
            for(int i = 0; i < times.length; i++) {
                if(times[i] > mid) break; 
                count += mid / times[i];  // mid라는 시간동안 times[i] 시간이 몇 명을 처리할 수 있는지
            }
            if(count < n) {
                start = mid + 1;
            } else {
                end = mid - 1;
                answer = mid;
            }
        }
        
        return answer;
    }

}