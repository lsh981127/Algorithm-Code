import java.util.*;
class Solution {
    
    public int solution(int distance, int[] rocks, int n) {
        Arrays.sort(rocks);
        int start = 1;
        int end = distance;
        int answer = 0;

        while(start <= end) {
            int count = 0;  // 부순 돌 갯수
            int mid = (start + end) / 2;
            int prev = 0;   // prev : 이전 돌의 거리
            for(int i : rocks) {
                if(i - prev < mid) {  // i번째 돌의 거리 - 이전 돌의 거리가 mid(우리가 정한 최소거리)보다 작으면 돌울 부수고
                    count++;
                } else {   // 최소 거리보다 크면, 내버려둬도 되니까 현재 돌은 유지하고 넘어가기 = prev에 현재 돌의 위치를 기억해두기
                    prev = i;          
                }
                
                // 이미 부숴야하는 돌보다 많이 부수면 의미 없으므로 반복문 탈출
                if(count > n) break;
            }
            // 위 for문은 rocks, 즉 돌들에 대해서만 최소 거리를 구한 경우
            // 마지막 돌 ~ end(distance)까지가 최소 거리인 경우에 대해서는 고려되지 않았다.
            if(distance - prev < mid) count++;
            
            if(count > n) {  // 부순 돌이 더 많으면 
                // 지금 설정한 최소거리(=mid)가 너무 길다는 뜻
                end = mid - 1;
            } else {
                // 현재 가질수 있는 최소거리를 구했다는 뜻
                // 단, 문제에서 최소값들 중 최대값을 구하는 것이기 때문에 left + 1해서 더 높은 경우를 찾는 것
                start = mid + 1;
                answer = mid;
            }
            
            
        }
        
        return answer;
    }

    
}