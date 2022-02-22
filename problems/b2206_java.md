## b2206

```java
import java.io.*;
import java.util.*;

public class _041_b2206 {
	static short[] delta_row = { -1, 1, 0, 0 };
	static short[] delta_col = { 0, 0, -1, 1 };
	
	public static void main(String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		String[] tmp = bf.readLine().split(" ");
		int ROW = Integer.parseInt(tmp[0]);
		int COL = Integer.parseInt(tmp[1]);
		
		int[][] matrix = new int[ROW][COL];
		boolean[][][] visited = new boolean[ROW][COL][2];
		for(int r=0; r<ROW; r++) {
			tmp = bf.readLine().split("");
			for(int c=0; c<COL; c++)
				matrix[r][c] = Integer.parseInt(tmp[c]);		
		}
		
		Queue<int[]> queue = new LinkedList<int[]>();
		queue.add(new int[] {0, 0, 0, 1});
		visited[0][0][0] = true;
		visited[0][0][1] = true;
		while(!queue.isEmpty()) {
			int[] q = queue.poll();
			int row = q[0];
			int col = q[1];
			int crash = q[2];
			
			if(row == ROW-1 && col == COL-1) {
				System.out.println(q[3]);
				return;
			}
			
			for(int i=0; i<4; i++) {
				int next_row = (row + delta_row[i]);
				int next_col = (col + delta_col[i]);
				
				if(0 > next_row || next_row >= matrix.length || 0 > next_col || next_col >= matrix[row].length) continue;
				
				if(matrix[next_row][next_col] == 0 && !visited[next_row][next_col][crash]) {
					queue.add(new int[] {next_row, next_col, crash, (q[3] + 1)});
					visited[next_row][next_col][crash] = true;
				}
				else if(matrix[next_row][next_col] == 1 && crash == 0) {
					queue.add(new int[] {next_row, next_col, 1, (q[3] + 1)});
					visited[next_row][next_col][1] = true;
				}
			}
		}		
		System.out.println(-1);
	}
}

```
