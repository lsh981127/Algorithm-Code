import java.util.*;
class Solution {
    static List<String> list;
    static String [] words = {"A", "E", "I", "O", "U"};

    // 처음에 그냥 조합으로 풀었다가 지문 다시 보니 순서가 달랐다.
    // 저 순서를 어떻게 해야할지 도무지 모르겠어서 참조..

    /**
     * ArrayList에 순서대로 값들을 넣는 방식
     * 0번째 인덱스는 "" 이기에 무의미하고 1번부터 A, AA, AAA 이런 식으로 넣어준다.
     */
    public int solution(String word) {
        int answer = 0;
        list = new ArrayList<>();
        dfs("", 0);
        int size = list.size();
        for (int i = 0; i < size; i++) {
            if (list.get(i).equals(word)) {
                answer = i;
                break;
            }
        }
        return answer;
    }
    static void dfs(String str, int len) {
        list.add(str);
        if (len == 5) return;
        // 계속해서 for문의 i = 0부터 값이 들어가기에 알파벳의 제일 앞값부터 들어간다
        
        for (int i = 0; i < 5; i++) {
            dfs(str + words[i], len + 1);
        }
    }
}