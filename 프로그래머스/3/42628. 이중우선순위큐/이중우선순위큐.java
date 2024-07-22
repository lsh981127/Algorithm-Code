import java.util.*;

class Solution {
    public static int[] solution(String[] operations) {
        PriorityQueue<Integer> maxPQ = new PriorityQueue<>((o1, o2) -> o1-o2);
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
                    maxPQ.offer(num * (-1));
                    minPQ.offer(num);
                    count++;
                    break;
                case "D":
                    ArrayDeque<Integer> dq = new ArrayDeque<>();
                    if(count == 0)
                        continue;
                    if(num == 1) {
                        maxPQ.poll();
                        // 최소 힙 제일 뒤에 있는 거 빼야해
                        for(int j = 0; j < count; j++) {
                            dq.offer(minPQ.poll());
                        }
                        for(int j = 0; j < count-1; j++) {
                            minPQ.add(dq.poll());
                        }
                    } else {
                        minPQ.poll();
                        for(int j = 0; j < count; j++) {
                            dq.offer(maxPQ.poll());
                        }
                        for(int j = 0; j < count-1; j++) {
                            maxPQ.add(dq.poll());
                        }

                    }
                    count--;
            }
        }
        System.out.println(Arrays.toString(maxPQ.toArray()));
        System.out.println(Arrays.toString(minPQ.toArray()));
        if(!maxPQ.isEmpty()) max = maxPQ.peek() * (-1);
        if(!minPQ.isEmpty()) min = minPQ.peek();


        int[] answer = {max, min};
        return answer;
    }
}