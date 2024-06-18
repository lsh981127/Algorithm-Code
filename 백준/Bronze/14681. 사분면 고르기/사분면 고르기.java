import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int x = sc.nextInt();
        int y = sc.nextInt();
        int xr = 0;
        int yr = 0;
        if (x > 0) xr = 1;
        if (y > 0) yr = 1;
        
        if ((xr == 1) & (yr == 1)) {
            System.out.println(1);
        } else if ((xr == 0) & (yr == 0)) {
            System.out.println(3);
        } else {
            if (x>0) {
               System.out.println(4);
            } else System.out.println(2);
        }
        
        
    }
}