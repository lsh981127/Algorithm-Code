import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> closet = new HashMap<>();
        for(String[] cloth : clothes) {
            closet.put(cloth[1], closet.getOrDefault(cloth[1], 0) + 1);
            // 기존 replace 를 사용해서 값을 변경하려 했으나 put을 넣어야 동작하더라
        }

//        Set<Map.Entry<String, Integer>> entry = closet.entrySet();
//        System.out.println(entry);
        for(Map.Entry<String, Integer> entry : closet.entrySet()) {
            answer *= entry.getValue() + 1;
        }
        return answer -1;
    }
}