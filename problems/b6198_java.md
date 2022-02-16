## b6198

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Stack;

public class _53_b6198 {
    public static void main (String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        long result = 0;

        Stack<Long> stack = new Stack<>();
        stack.push(sc.nextLong());
        N--;
        while(N-- > 0) {
            long nxt = sc.nextLong();
            while(!stack.isEmpty() && stack.peek() <= nxt)
                stack.pop();
            result += stack.size();
            stack.push(nxt);
        }
        System.out.println(result);
    }
}
```
