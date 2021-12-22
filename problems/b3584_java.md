## b3584

```java
import java.io.*;
import java.util.*;

public class _021_b3584 {
	static int[] parent;
	static ArrayList<ArrayList<Integer>> child;
	public static void main(String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		int tc = Integer.parseInt(bf.readLine());
		for(int t=0; t<tc; t++) {
			int n = Integer.parseInt(bf.readLine());
			child = new ArrayList<ArrayList<Integer>>();

			for(int i=0; i<n+1; i++) child.add(new ArrayList<Integer>());

			parent = new int[n+1];
			for(int i=0; i<n-1; i++) {
				String[] tmp = bf.readLine().split(" ");
				int a = Integer.parseInt(tmp[0]);
				int b = Integer.parseInt(tmp[1]);
				parent[b] = a;
				child.get(a).add(b);
			}

			String[] tmp = bf.readLine().split(" ");
			int a = Integer.parseInt(tmp[0]);
			int b = Integer.parseInt(tmp[1]);

			int a_depth = get_depth(a);
			int b_depth = get_depth(b);

			System.out.println(solve(a, b, a_depth, b_depth));
		}
	}

	private static int solve(int a, int b, int a_depth, int b_depth) {
		int reulst = 0;
		if(a_depth > b_depth) {
			while(a_depth != b_depth) {
				a_depth--;
				a = parent[a];
			}
		}
		else if(a_depth < b_depth) {
			while(a_depth != b_depth) {
				b_depth--;
				b = parent[b];
			}
		}
		while(a != b) {
			a = parent[a];
			b = parent[b];
		}

		return a;
	}

	private static int get_depth(int a) {
		int depth = 0;

		while(parent[a] != 0) {
			depth++;
			a = parent[a];
		}
		return depth;
	}

}


```
