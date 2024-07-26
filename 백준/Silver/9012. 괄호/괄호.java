import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        for(int a = 0; a < N; a++) {
            int left = 0;
            int right = 0;
            String s = br.readLine();
            for(char i : s.toCharArray()) {
                if(i == ')') {
                    right++;
                    if(left != 0) {
                        left--;
                        right--;
                    } else {
                        break;
                    }
                }

                if(i == '(') {
                    left++;
                    if(right != 0) {
                        left--;
                        right--;
                    }
                }
            }
            if(left != 0 || right != 0)
                System.out.println("NO");
            else System.out.println("YES");
        }
        
        
    }
}