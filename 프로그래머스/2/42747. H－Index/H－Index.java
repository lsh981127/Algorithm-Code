import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int index = 0;
        int size = citations.length;
        int answer = 0;
        Integer[] reverse = Arrays.stream(citations).boxed().toArray(Integer[]::new);
        
        Arrays.sort(reverse, (a, b) -> b - a); 
        for(int i = 0; i < size; i++) {
            if(reverse[i] < i+1) {
                answer = i;
                return answer;
            }
        }
        return size;
    }
}