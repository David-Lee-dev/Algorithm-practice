## b1325

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class _058_b1325 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp = bf.readLine().split(" ");

        int N = Integer.parseInt(tmp[0]);
        int M = Integer.parseInt(tmp[1]);

        int[] possible = new int[N+1];
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        for(int i=0; i<=N; i++) list.add(new ArrayList<Integer>());
        for(int i=0; i<M; i++){
            tmp = bf.readLine().split(" ");
            int a = Integer.parseInt(tmp[0]);
            int b = Integer.parseInt(tmp[1]);

            list.get(a).add(b);
        }

        for(int i=1; i<=N; i++) {
            boolean[] hacked = new boolean[N+1];
            bfs(i, hacked, list, possible);
        }

        int max = 0;
        for(int i=1; i<=N; i++) {
            max = Math.max(max, possible[i]);
        }
        StringBuffer sb = new StringBuffer();
        for(int i=1; i<=N; i++) {
            if(possible[i] == max)
                sb.append(i+" ");
        }
        System.out.println(sb.toString());
    }
    private static void bfs (int idx, boolean[] hacked, ArrayList<ArrayList<Integer>> list, int[] possible) {
        Queue<Integer> queue = new LinkedList<>() ;
        queue.add(idx);
        hacked[idx] = true;

        while(!queue.isEmpty()){
            int now = queue.poll();
            for(int i=0; i<list.get(now).size(); i++) {
                int v = list.get(now).get(i);
                if(!hacked[v]) {
                    hacked[v] = true;
                    possible[v]++;
                    queue.add(v);
                }
            }
        }
    }
}

```
