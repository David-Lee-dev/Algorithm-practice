## b1700
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _051_b1900 {
    static int result = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp = bf.readLine().split(" ");
        int N = Integer.parseInt(tmp[0]);
        int K = Integer.parseInt(tmp[1]);

        int[] mt = new int[N];
        int[] order = new int[K];
        tmp = bf.readLine().split(" ");
        for(int i=0; i<K; i++) order[i] = Integer.parseInt(tmp[i]);

        int idx = 0;
        int i = 0;
        while(i < N){
            if(checkMT(mt,order[idx]) < 0) {
                mt[i++] = order[idx];
            }
            idx++;
        }

        while(idx < K) {
            if(checkMT(mt, order[idx]) < 0) {
                mt[choice(mt, order, idx)] = order[idx];
                result++;
            }
            idx++;
        }
        System.out.println(result);
    }
    private static int checkMT (int[] mt, int num) {
        for(int i=0; i<mt.length; i++)
            if(mt[i] == num) return i;

        return -1;
    }
    private static int choice (int[] mt, int[] order, int start) {
        int[] cnt = new int[order.length]; // 추후 사용 횟수
        int last = 0; // 가장 나중에 사용하는 것
        for(int i=start+1; i<order.length; i++) {
            cnt[order[i]-1]++;
            int tmp = checkMT(mt, order[i]);
            if(tmp >= 0 && cnt[order[i]-1] == 1 ) last = tmp;
        }

        for(int i=0; i<cnt.length; i++){
            int tmp = checkMT(mt, i);
            if(tmp < 0) continue;
            if(cnt[i-1] == 0) return tmp;
        }

        return last;
    }
}
```