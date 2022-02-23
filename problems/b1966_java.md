## b1966

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class _056_b01966 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(bf.readLine());

        String[] tmp;
        while(tc-- > 0) {
            tmp = bf.readLine().split(" ");
            int N = Integer.parseInt(tmp[0]);
            int M = Integer.parseInt(tmp[1]);
            int cnt = 0;

            tmp = bf.readLine().split(" ");
            PriorityQueue<Priority> pq = new PriorityQueue<>();
            Queue<int[]> q = new LinkedList<>();

            for(int i=0; i<N; i++) {
                pq.add(new Priority(Integer.parseInt(tmp[i])));
                q.add(new int[] {i, Integer.parseInt(tmp[i])});
            }

            while(!q.isEmpty()){
                int[] q_peek = q.poll();
                Priority pq_peek = pq.peek();

                if(q_peek[1] != pq_peek.num) q.add(q_peek);
                else {
                    if(q_peek[0] == M) {
                        System.out.println(++cnt);
                        break;
                    }
                    pq.poll();
                    cnt++;
                }
            }
        }
    }
}

class Priority implements Comparable<Priority> {
    int num;

    public Priority(int num){
        this.num = num;
    }

    @Override
    public int compareTo(Priority p) {
        return p.num - this.num;
    }
}


```
