## b4796

```java
import java.io.*;
import java.util.*;

public class _025_b4796 {
	public static void main(String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int tc = 1;
		while(true) {
			String[] st = bf.readLine().split(" ");
			int L = Integer.parseInt(st[0]);
			int P = Integer.parseInt(st[1]);
			int V = Integer.parseInt(st[2]);
			if(L == 0) return;

			int result = ((V / P) * L) + ((V % P) > L? L:(V % P));
			System.out.printf("Case %d: %d\n", tc, result);
			tc++;
		}
	}
}
```
