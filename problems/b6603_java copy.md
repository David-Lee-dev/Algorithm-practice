## b9934

```java
import java.io.*;
import java.util.*;

public class _020_b9934 {
	static int[] result;
	public static void main(String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());

		int K = Integer.parseInt(st.nextToken());
		int n = (int) Math.pow(2, K) - 1;

		st = new StringTokenizer(bf.readLine());
		int[] tree = new int[n];
		result = new int[n];
		for(int i=0; i<n; i++) tree[i] = Integer.parseInt(st.nextToken());

		traversal(tree, 0, n, 0);
		print(K);
	}
	private static void traversal(int[] tree, int s, int e, int depth) {
		int m = (s + e) / 2;
		int idx = (int) Math.pow(2, depth) - 1;

		while(result[idx] != 0) idx++;
		result[idx] = tree[m];

		if(m == s || m == e) return;

		traversal(tree, s, m, depth+1);
		traversal(tree, m+1, e, depth+1);
		return;
	}
	private static void print(int K) {
		for(int i=0; i<K; i++) {
			for(int j=(int)Math.pow(2, i)-1;j<(int)Math.pow(2, i+1)-1;j++) {
				System.out.printf("%d ", result[j]);
			}
			System.out.println();
		}
	}
}

```
