class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        // Array of Sum
        const int n = nums.size();
        
        // pref[L...R] = pref[R] - pref[L-1] = k + pref[R]
        int ans = 0;
        int pref = 0;
        
        unordered_map<int,int>sum_freq;
        sum_freq[pref]++;
        for(int i = 0; i < n; i++) {
            pref += nums[i];
            int find = pref - k;
            ans += sum_freq[find];
            sum_freq[pref]++;
        }
        
        return ans;
    }
};
