## b1012
```java
import java.io.*;
import java.util.*;

public class _044_b1012 {
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};
	static int result;
	
	 public static void main(String args[]) throws IOException {
		 BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		 
		 int tc = Integer.parseInt(bf.readLine());
		 while(tc-- > 0) {
			 String[] tmp = bf.readLine().split(" ");
			 int col = Integer.parseInt(tmp[0]);
			 int row = Integer.parseInt(tmp[1]);
			 int[][] matrix = new int[row][col];
			 boolean[][] visited = new boolean[row][col];
			 
			 int K = Integer.parseInt(tmp[2]);
			 while(K-- > 0) {
				 tmp = bf.readLine().split(" ");
				 matrix[Integer.parseInt(tmp[1])][Integer.parseInt(tmp[0])] = 1;
			 }
			 result = 0;
			 for(int r=0; r<row; r++) {
				 for(int c=0; c<col; c++) {
					 if(matrix[r][c] == 1 && !visited[r][c])
						 BFS(matrix, visited, r, c);
				 }
			 }
			 System.out.println(result);
		 }
	 }
	 private static void BFS(int[][] matrix, boolean[][] visited, int row, int col) {
		 Queue<int[]> q = new LinkedList<int[]>();
		 q.add(new int[] {row, col});
		 visited[row][col] = true;
		 result++;
		 
		 while(!q.isEmpty()) {
			 int[] cur = q.poll();
			 int r = cur[0];
			 int c = cur[1];
			 
			 for(int i=0; i<4; i++) {
				 int nr = cur[0] + dr[i];
				 int nc = cur[1] + dc[i];
				 if(0 > nr || nr >= matrix.length || 0 > nc || nc >= matrix[r].length) continue;
				 if(matrix[nr][nc] == 1 && !visited[nr][nc]) { 
					 visited[nr][nc] = true;
					 q.add(new int[] {nr, nc});
				 }
			 }
		 }
	 }
}


```