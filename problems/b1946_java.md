## b1946

```java
import java.util.*;
import java.io.*;

public class _024_b1946 {
	public static void main(String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(bf.readLine());
		while(T-- > 0) {
			int N = Integer.parseInt(bf.readLine());
			int[][] rank = new int[N][2];

			for(int i=0; i<N; i++) {
				String[] tmp = bf.readLine().split(" ");
				rank[i][0] = Integer.parseInt(tmp[0]);
				rank[i][1] = Integer.parseInt(tmp[1]);
			}

			Arrays.sort(rank, new Comparator<int[]>() {
				@Override
					public int compare(int[] o1, int[] o2) {
						return o1[0] - o2[0];
				}
			});
			int interview_min = rank[0][1];
			int cnt = 1;
			for(int i=1; i<N; i++) {
				if(rank[i][1] < interview_min) {
					cnt++;
					interview_min = rank[i][1];
				}
			}
			System.out.println(cnt);
		}
	}
}


```
