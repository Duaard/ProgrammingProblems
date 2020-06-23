class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int H = grid.size();
        int W = grid[0].size();
        vector<vector<int>> dp(H, vector<int>(W));
        for(int row = 0; row < H; row++) {
            for(int col = 0; col < W; col++) {
                if(row == 0 && col == 0) {
                    dp[row][col] = grid[row][col];
                } else {
                    dp[row][col] = grid[row][col] + min(col==0?INT_MAX:dp[row][col-1], row==0?INT_MAX:dp[row-1][col]);
                }
            }
        }
        
        return dp[H-1][W-1];
    }
};
