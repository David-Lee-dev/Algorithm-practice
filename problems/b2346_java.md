## b2346

```java
import java.util.*;
import java.io.*;

public class _040_b2346 {
	public static void main(String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(bf.readLine());
		String[] tmp = bf.readLine().split(" ");
		
		Deque<int[]> arr = new ArrayDeque<int[]>();
		for(int i=0; i<N; i++) arr.add(new int[] {Integer.parseInt(tmp[i]), i+1});;
		
		int[] next = arr.pollFirst();
		int move = next[0];
		System.out.printf("%d ", next[1]);
		while(!arr.isEmpty()) {
			if(move > 0) {
				for(int i=1; i<move; i++) arr.addLast(arr.pollFirst());
				
				next = arr.pollFirst();
				move = next[0];
				System.out.printf("%d ", next[1]);
			}
			else {
				for(int i=move; i<-1; i++) arr.addFirst(arr.pollLast());
				
				next = arr.pollLast();
				move = next[0];
				System.out.printf("%d ", next[1]);
			}
		}
	}
}

```
