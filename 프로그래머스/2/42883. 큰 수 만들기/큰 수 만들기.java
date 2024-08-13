import java.util.*;
class Solution {
    
    // https://velog.io/@joonghyun/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%EC%9E%90%EB%B0%94
    public String solution(String number, int k) throws Exception{
        
        // k 자리를 뺀다 = number.size() - k 개 자리만 고려한다.
        
        // 뒤에서부터 구해야하는 자리수 만큼 남겨두고 생각하기
        int len = number.length() - k;
        int start = 0;
        char[] num = number.toCharArray();
        StringBuilder sb = new StringBuilder();
        String answer = "";
        for(int i = 0; i < len; i++) {
            // i는 뽑은 자릿수
            char max = '0';
            for(int j = start; j <= i+k;j++) {
                // start 지점부터 i번째 자리+ 잘라야할 k개
                if(num[j] > max) {
                    max = num[j];
                    start = j + 1;
                    // j번째를 넣으면, j+1번째부터 탐색하게 하기 위해
                }
            }
            sb.append(max);
        }
        
        return sb.toString();
    }
}