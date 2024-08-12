import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        // n : 학생 수
        // Lost : 잃어버린 학생 번호
        // reserve : 가지고 있는 학생 번호
        
        int answer = n;
        
        Set<Integer> lostS = new HashSet<>();
        Set<Integer> reserveS = new HashSet<>();
        
        for(int i : reserve) {
            reserveS.add(i);
        }
        
        for(int i : lost) {
            if(reserveS.contains(i)){
                reserveS.remove(i);
            } else {
                lostS.add(i);
            }
        }
        
        // 그르네, 굳이 잃어버린 애들 기준으로 생각할 필요가 없네
        // 남은 애들 기준으로 왼,오 판단해서 removeS를 줄이고 길이만 사용하면 되네
        for(Integer i : reserveS) {
            if(lostS.contains(i-1)) {
                lostS.remove(i-1);
            } else if(lostS.contains(i+1)) {
                lostS.remove(i+1);
            }
        }
        
        return n - lostS.size();
        
    }
}