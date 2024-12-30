import java.util.*;
import java.io.*;
public class Main {
    static int answer = (int) 10e9;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long A = Integer.parseInt(st.nextToken());
        long B = Integer.parseInt(st.nextToken());

        cal(A, B, 0);
        if(answer != (int) 10e9) System.out.println(answer + 1);
        else System.out.println(-1);

    }

    static void cal(long current, long B, int count) {
        if(current > B) return ;
        if(current == B) {
            if(answer > count) answer = count;
            return ;
        }

        cal(current * 2, B, count+1);
        cal(current * 10 + 1, B, count+1);

    }
}
