import java.util.*;
import java.io.*;

public class Main {
    
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int val = a;        
        if(a == b && b == c) {
            System.out.println(10000+ 1000*val);
        } else if((a == b)|| (b ==c) || (a==c)) {
            if(b == c) {
                val = b;
            }
            System.out.println(1000+ 100*val);
            
        } else {
            if(val < b) val = b;
            if(val < c) val = c;
            System.out.println(val * 100);
        }
    }
}