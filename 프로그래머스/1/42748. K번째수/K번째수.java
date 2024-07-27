import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int y = 0; y < commands.length; y++) {
            int[] arr = commands[y];
            int i = arr[0]-1, j = arr[1]-1, k = arr[2]-1;
            int[] temp = new int[j-i+1];
            for(int x = 0; x < j-i + 1; x++) {
                temp[x] = array[i+x];
            }
            Arrays.sort(temp);
            answer[y] = temp[k];
        }

        return answer;
    }
}