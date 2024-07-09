import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> set = new HashSet<>();
            for (int i = 0; i < phone_book.length; i++) {
                set.add(phone_book[i]);
            }

            for (int i = 0; i < phone_book.length; i++) {
                // 각 값들에 대해
                for (int j = 0; j < phone_book[i].length(); j++) {
                    // 길이 0부터 해당 길이까지 해당 값들의 Key가 존재하는지 확인하는 거야
                    // O(N^2)라서 다른 방법 없나 고민했는데 더 좋은 아이디어가 없어서 ㅠ
                    // 1,000,000 ^ 2  = 10^12
                    if (set.contains(phone_book[i].substring(0, j))) {
                        return false;
                    }
                }
            }

            return true;
    }
}