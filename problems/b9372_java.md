## b9372

```java
import java.io.*;
import java.util.*;

public class _019_b9372 {
	static int[][] matrix;
	static boolean[] visited;
	static int result;
	public static void main(String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());

		int T = Integer.parseInt(st.nextToken());

		for(int tc=0; tc<T; tc++) {
			st = new StringTokenizer(bf.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());

			matrix = new int[N+1][N+1];
			result = N*M;
			for(int i=0; i<M; i++) {
				st = new StringTokenizer(bf.readLine());
				int src = Integer.parseInt(st.nextToken());
				int dst = Integer.parseInt(st.nextToken());
				matrix[src][dst] = 1;
				matrix[dst][src] = 1;
			}
			System.out.println(N-1);
		}
	}
}

```
