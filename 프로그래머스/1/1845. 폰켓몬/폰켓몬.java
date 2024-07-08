import java.util.*;
class Solution {
    public int solution(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i: nums) {
            if(map.containsKey(i)) continue;
            map.put(i, 1);
        }
        
        
        int answer = map.entrySet().size();
        
        if(answer > nums.length / 2) {
            answer = nums.length / 2;
        } 
        return answer;
    }
}