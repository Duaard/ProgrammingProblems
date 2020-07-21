class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        const int n = piles.size();

        vector<vector<pair<int, int>>> dp(n, vector< pair<int,int> >(n));
    
        for(int L = n - 1; L >= 0; L--) {
            for(int R = L; R < n; R++) {
                if(L == R) {
                    dp[L][R] = make_pair(piles[L], 0);
                    continue;
                }
                //cout << "[L][R] is: " << L << ", " << R << "\n";
                pair<int,int> l = make_pair(dp[L + 1][R].second + piles[L], dp[L+1][R].first);
                pair<int,int> r = make_pair(dp[L][R-1].second + piles[R], dp[L][R-1].first);
                
                dp[L][R] = l.first - l.second > r.first - r .second ? l : r;
            }
        }
    
        return dp[0][n-1].first > dp[0][n-1].second;
    }
};
