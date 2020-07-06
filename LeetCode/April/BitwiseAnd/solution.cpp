class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        if(m == n) {
            return m;
        }
        int bit = m;
        for(unsigned int i = m; i <= n; i++) {
            if(bit == 0) {
                return 0;
            }
            bit &= i;
        }
        return bit;
    }
};
