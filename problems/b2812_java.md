## b2812

```java
import java.util.*;
import java.io.*;

public class _026_b2812 {
	public static void main(String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder result = new StringBuilder();
		String[] tmp = bf.readLine().split(" ");

		int N = Integer.parseInt(tmp[0]);
		int K = Integer.parseInt(tmp[1]);
		int cnt = K;

		String st_tmp = bf.readLine();
		int[] numbers = new int[N];
		for(int i=0; i<N; i++) {
			numbers[i] = st_tmp.charAt(i) - 48;
		}
		Stack<Integer> stack = new Stack<Integer>();
		for(int i=0; i<numbers.length; i++) {
			while(cnt > 0 && !stack.isEmpty() && stack.get(stack.size() - 1) < numbers[i]) {
				stack.pop();
				cnt--;
			}
			stack.push(numbers[i]);

		}

		for(int i=0; i<N-K; i++) {
			result.append(stack.get(i));
		}
		System.out.println(result);
	}
}

```
