import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        
        // 처음에는 그냥 오름차순 정렬 -> 작은 애들 순서로 채우기
        // 반례 존재, 30 50 50 70
        // 작은 애를 뽑았으면 채울 수 있는 애들 중 가장 큰 애랑 태우기
        
        int answer = 0;
        int left= 0;
        int right = people.length - 1;
        Arrays.sort(people);
        
        while(left < right) {
            int lw = people[left];
            int rw = people[right];
            if(lw + rw <= limit) {
                answer++;
                left++;
                right--;
            } else {
                right--;
            }
        }
                
        return people.length - answer;
    }
}