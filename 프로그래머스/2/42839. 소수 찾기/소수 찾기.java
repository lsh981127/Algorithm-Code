import java.util.*;
class Solution {
    
    static Set<Integer> set;
    static boolean[] visited;
    public static int solution(String numbers) {
        // 조합 사용
        // 각 값들을 소수 판별

        // 참조한 과정
        // 조합
        // 각 값을 Set에 넣고
        // 이 Set에 존재하는 값들에 대해서만 소수 판별

        set = new HashSet<>();
        visited = new boolean[7];
        
        for(int i = 0; i < numbers.length(); i++) {
            comb(numbers, "", i+1);
        }


        int answer = 0;
        for(Integer i : set) {
            if(prime(i)) {
                answer++;
            }
        }

        return answer;
    }

    static boolean prime(int n) {
        if(n < 2) return false;

        for(int i = 2; i <= (int) Math.sqrt(n); i++) {
            if(n % i == 0) return false;
        }

        return true;

    }

    static void comb(String numbers, String current, int count) {
        if(count == current.length()) {
            int num = Integer.parseInt(current);
            System.out.println(num);
            set.add(num);
            return;
        }

        for(int i = 0; i < numbers.length(); i++) {
            if(!visited[i]) {
                visited[i] = true;
                comb(numbers, current + numbers.charAt(i), count);
                visited[i] = false;
            }
        }
    }
    
}