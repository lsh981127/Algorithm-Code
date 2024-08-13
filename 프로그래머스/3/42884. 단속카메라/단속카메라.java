import java.util.*;
class Solution {
    public int solution(int[][] routes) {
        // 지문을 잘못 이해했다.
        // 전부 다 연결해야하는 방법으로 이해를 했다.
        
        // 그냥 다음 차 진입 시점을 못찍어?(더 커)
        // 그러면, 카메라를 다음 차 진입 시점에 한 개 더 추가
        
        Arrays.sort(routes, (o1, o2) ->
                    o1[1] == o2[1] ? o1[0] - o2[0] : o1[1]-o2[1]);
        
        // 끝나는 시점 기준 오름차순 정렬
        
        int answer = 1;
        int end = routes[0][1];
        
        for(int i = 1; i < routes.length; i++) {
            if(end < routes[i][0]) {
                // 지금 끝나는 지점보다 다음 차량의 시작이 더 늦으면
                // 카메라로 찍을 수 없어서 다음 차 시작 부분에 카메라 추가 설치
                answer++;
                end = routes[i][1];
            }
        }
        return answer;
    }
}