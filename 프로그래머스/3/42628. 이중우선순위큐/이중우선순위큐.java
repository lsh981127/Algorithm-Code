import java.util.*;

class Solution {
    public static int[] solution(String[] operations) {
        PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Comparator.reverseOrder());
        PriorityQueue<Integer> minPQ = new PriorityQueue<>((o1, o2) -> o1-o2);
        int max = 0;
        int min = 0;
        int count = 0;
        for(String i : operations) {
            String[] temp = i.split(" ");
            String func = temp[0];
            int num = Integer.parseInt(temp[1]);
            switch(func) {
                case "I":
                    maxPQ.offer(num);
                    minPQ.offer(num);
                    count++;
                    break;
                case "D":
                    ArrayDeque<Integer> dq = new ArrayDeque<>();
                    if(count == 0)
                        continue;
                    if(num == 1) {
                        int search = maxPQ.poll();
                        if(minPQ.contains(search)) minPQ.remove(search);
                    } else {
                        int search = minPQ.poll();
                        if(maxPQ.contains(search)) maxPQ.remove(search);

                    }
                    count--;
            }
        }
        
        if(!maxPQ.isEmpty()) max = maxPQ.peek();
        if(!minPQ.isEmpty()) min = minPQ.peek();


        int[] answer = {max, min};
        return answer;
    }
}