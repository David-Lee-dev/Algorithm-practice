## b4693
```java
import java.util.*;
import java.io.*;
public class _042_b4963 {
	static int[] delta_row = {-1, -1, -1, 0, 1, 1, 1, 0};
	static int[] delta_col = {-1, 0, 1, 1, 1, 0, -1, -1};
	static boolean land;
	static int result;
	public static void main (String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			String[] tmp = bf.readLine().split(" ");
			int COL = Integer.parseInt(tmp[0]);
			int ROW = Integer.parseInt(tmp[1]);
			if(ROW == 0 && COL  == 0) break;
			int[][] matrix = new int [ROW][COL];
			boolean[][] visited = new boolean[ROW][COL];
			
			for(int r=0; r<ROW; r++) {
				tmp = bf.readLine().split(" ");
				for(int c=0; c<COL; c++) {
					matrix[r][c] = Integer.parseInt(tmp[c]);
				}
			}
			result = 0;
			for(int r=0; r<ROW; r++) {
				for(int c=0; c<COL; c++) {
					land = false;
					if (!visited[r][c] && matrix[r][c] == 1) DFS(matrix, visited, r, c);
					else visited[r][c] = true;
					if(land) result++;
				}
			}			
			System.out.println(result);
		}
	}
	private static void DFS(int[][] matrix, boolean[][] visited, int row, int col) {
		visited[row][col] = true;
		if(matrix[row][col] == 1) land=true;
		
		for(int i=0; i<8; i++) {
			int nr = row + delta_row[i];
			int nc = col + delta_col[i];
			
			if(0 > nr || nr >= matrix.length || 0 > nc || nc >= matrix[row].length) continue;
			if(matrix[nr][nc] == 1 && !visited[nr][nc]) DFS(matrix, visited, nr, nc);
		}
	}
}

```