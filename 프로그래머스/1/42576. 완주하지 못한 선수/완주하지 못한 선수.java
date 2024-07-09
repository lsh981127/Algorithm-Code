import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < participant.length; i++) {
            if (map.containsKey(participant[i])) {
                map.put(participant[i], map.get(participant[i]) + 1);
            } else {
                map.put(participant[i], 1);
            }
        }

        for (int i = 0; i < completion.length; i++) {
            if (map.containsKey(completion[i])) {
                map.put(completion[i], map.get(completion[i]) - 1);
                if (map.get(completion[i]) == 0) {
                    map.remove(completion[i]);
                }
            }
        }
        
        for (String s : map.keySet()) {
            sb.append(s);
        }
        
        return sb.toString();
    }
}