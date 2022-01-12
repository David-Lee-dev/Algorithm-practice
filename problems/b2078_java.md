## b2078

```java
import java.util.*;
import java.io.*;

public class _034_b2078 {
	static final int LEFT = 0;
	static final int RIGHT = 1;

	public static void main(String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		String[] tmp = bf.readLine().split(" ");
		int[] input = {Integer.parseInt(tmp[0]), Integer.parseInt(tmp[1])};

		int a = input[LEFT];
		int b = input[RIGHT];
		int left = 0;
		int right = 0;

		while(a > 1 || b > 1) {
			if(a > b) {
				a = a - b;
				left++;
			}
			else {
				b = b - a;
				right++;
			}
		}
		System.out.printf("%d %d", left, right);
	}
}

```
