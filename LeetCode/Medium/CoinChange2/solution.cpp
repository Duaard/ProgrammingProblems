class Solution {
public:
    int change(int amount, vector<int>& coins) {
        const int n = coins.size();
        vector<vector<int>> dp(amount+1, vector<int>(n));
        
        for(int i = 0; i < amount + 1; i++) {
            for(int k = 0; k < n; k++) {
                
            }
        }
        
        
        return dp[amount][n];
    }
};
