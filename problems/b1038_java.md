## b1158

```java
import java.io.*;
import java.util.*;

public class _034_b1038 {
	static int cnt = 0;
	static boolean end = false;
	static final int MAX_NUM = 1000000;

	public static void main(String args[]) throws IOException {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		if(N < 10) System.out.println(N);

		else {
			Deque<Integer> dq = new ArrayDeque<Integer>();
			cnt = 9;
			int leng = 2;
			while(!end && leng < 11) {
				for(int num=leng-1; num<10; num++) {
					dq.addLast(num);
					BT(dq, leng, N);
					if(end) break;
					dq.removeLast();
				}
				leng++;
			}
			String result = leng < 12 ? cal(dq):"-1";
			System.out.println(result);
		}
	}

	private static void BT(Deque<Integer> dq, int leng, int N) {
		for(int i=0; i<10; i++) {
			if(cnt == N) {
				end = true;
				return;
			}
			if(dq.size() < leng-1) {
				if(dq.getLast() <= i) return;
				dq.addLast(i);
				BT(dq, leng, N);
				if(cnt != N) dq.removeLast();
			}
			else if(dq.getLast() > i) {
				cnt++;
				if(cnt == N) dq.addLast(i);
			}
			else return;
		}
	}

	private static String cal(Deque<Integer> dq) {
		String[] result = new String[dq.size()];
		int size = dq.size();
		for(int i=size-1; i >= 0; i--) {
			result[i] = Integer.toString(dq.removeLast());
		}
		return String.join("", result);
	}
}

```
