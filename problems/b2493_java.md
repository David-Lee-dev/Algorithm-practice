## b2493

```java
import java.io.*;
import java.util.Stack;

public class _054_b2493 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String[] tmp = bf.readLine().split(" ");
        int N = Integer.parseInt(tmp[0]);

        int[] result = new int[N+1];
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[] {0, 0});

        tmp = bf.readLine().split(" ");
        for(int i=1; i<= tmp.length; i++) {
            int t = Integer.parseInt(tmp[i-1]);
            while(!stack.isEmpty()){
                if(stack.peek()[0] >= t) {
                    break;
                }
                stack.pop();
            }
            if(stack.isEmpty()) result[i] = 0;
            else result[i] = stack.peek()[1];
            stack.push(new int[] {t, i});
            sb.append(result[i]).append(" ");
        }
        System.out.println(sb);
    }
}

```
