## b2644
```java
import java.io.*;
import java.util.StringTokenizer;

public class _007_b2644 {
	static int result = -1;
	static byte[] visited;
	static int[][] matrix;
	private static void DFS(int s, int d, int count, int size) {
		if(s == d) {
			result = count;
			return;
		}
		
		visited[s] = 1;
		for(int i = 1; i<size; i++) {
			if (matrix[s][i] == 1 && visited[i] == 0) {
				DFS(i, d, count+1, size);
			}
		}
	}
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()); // 찾아야 하는 사람 입력
		
		int n = Integer.parseInt(st.nextToken()); // 사람 수 입력
		visited = new byte[n+1];
		matrix = new int[n+1][n+1];
		
		st = new StringTokenizer(br.readLine()); // 촌수 계산할 사람 입력
		int s = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine()); // 촌수 정보 개수 입력
		int m = Integer.parseInt(st.nextToken());
		
		// 인접행렬 생성
		while(m-- > 0) {
			st = new StringTokenizer(br.readLine());
			int[] buffer = {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
			matrix[buffer[0]][buffer[1]] = 1;
			matrix[buffer[1]][buffer[0]] = 1;
		}
		DFS(s, d, 0, n+1);
		System.out.println(result);
	}
}

```