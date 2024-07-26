import java.util.*;
import java.io.*;
class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int count = 0;
        int num = 665;
        while(count != N) {
            num++;
            if(String.valueOf(num).contains("666")) {
                count++;
            }
        }

        System.out.println(num);
    }
}
