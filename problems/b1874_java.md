## b1874

```java
import java.io.*;
import java.util.*;

public class _038_b1874 {
	public static void main(String args[]) throws IOException{
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] tmp = new int[N];
		for(int i=0; i<N; i++) tmp[i] = sc.nextInt();
		
		int num = 1;
		int idx = 0;
		Stack<Integer> stack = new Stack<Integer>();
		Stack<Character> result = new Stack<Character>();
		
		while(idx < N) {
			if(!stack.isEmpty() && num > N && tmp[idx] != stack.peek()) break;
			if(!stack.isEmpty() && tmp[idx] == stack.peek()) {
				result.push('-');
				stack.pop();
				idx++;
				if(idx == N) break;
				continue;
			}
			else {				
				stack.push(num);
				result.push('+');
				num++;
			}
		}
		
		if(idx >= N) for(int i=0; i<result.size(); i++) System.out.println(result.get(i));
		else System.out.println("NO");
	} 
}

```
