## b1461

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class _052_b1461 {
    public static  void  main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String[] tmp = bf.readLine().split(" ");
        int N = Integer.parseInt(tmp[0]);
        int M = Integer.parseInt(tmp[1]);

        int[] books = new int[N+1];
        books[N] = 0;
        tmp = bf.readLine().split(" ");
        for(int i=0; i<N; i++) books[i] = Integer.parseInt(tmp[i]);
        Arrays.sort(books);

        Deque<Integer> table = new ArrayDeque<>(N);
        for(int i=0; i<N+1; i++) table.addLast(books[i]);
        int minus = Math.abs(table.getFirst()) > Math.abs(table.getLast()) ? table.getFirst() : table.getLast();

        int result = 0;
        while (table.size() > 1) {
            result += (Math.abs(table.getFirst()) + Math.abs(table.getLast())) * 2;

            for(int i=0; i<M; i++){
                if(table.getFirst() == 0) break;
                table.removeFirst();
            }
            for(int i=0; i<M; i++){
                if(table.getLast() == 0) break;
                table.removeLast();
            }
        }
        System.out.println(result - Math.abs(minus));
    }
}

```
