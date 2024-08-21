class Solution {
    // 근데 이 방법이 되네;;
    // dp 다운업 방식
    // 그냥 반복문 돌면서 왼쪽 위, 오른쪽 위 중 더 큰 값과 더하는 방식
    // 제일 마지막번째 배열에서 가장 큰 값을 구하면 되는 거야
    
    
    
    public int solution(int[][] triangle) {
        for(int i = 1; i < triangle.length; i++) {
            int[] temp = triangle[i];
            int len = temp.length;
            for(int j = 0; j < len; j++) {
                // index 본인과, 본인 index - 1 애들의 합
                int left = 0, right = 0;
                if(j-1 >= 0) left = triangle[i-1][j-1];
                if(j < len - 1) right = triangle[i-1][j];
                
                // 더 큰 것과 더해서 저장
                triangle[i][j] += Math.max(left, right);
            }
        }
        
        // 제일 마지막째 줄의 최댓값만 구하면 돼.
        
        int answer = 0;
        for(int i: triangle[triangle.length-1]) {
            if(i > answer) answer = i;
        }
        
        return answer;
    }
}