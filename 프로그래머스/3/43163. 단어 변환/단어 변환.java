import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        ArrayDeque<String> dq = new ArrayDeque<>();
        Set<String> set = new HashSet<>(Arrays.asList(words));

        int count = 0;
        if(!set.contains(target)) return count;

        dq.offer(begin);
        set.remove(begin);

        while(!dq.isEmpty()) {
            for(int i = 0; i < dq.size(); i++) {
                // dq에 남아있는 애들 중, set에 있는 애들과 1개밖에 차이 안나는 애들을 찾아야함
                String temp = dq.poll();
                if(temp.equals(target)) return count;


                for(String word : set.toArray(new String[set.size()])) {
                    int diff = 0;
                    for(int j = 0; j < word.length(); j++) {
                        if(word.charAt(j) != temp.charAt(j)) diff++;
                    }

                    if(diff == 1) {
                        dq.offer(word);
                        set.remove(word);
                    }
                }
            }
            count++;

        } 
        return count;
    }
}