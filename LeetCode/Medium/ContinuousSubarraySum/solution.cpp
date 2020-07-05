class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        const int n = nums.size();
        int sum = 0;
        unordered_map<int,int> map;
        map[sum] = -1;
        for(int i = 0; i < n; i++) {
            sum += nums[i];
            if (k != 0) sum %= k;
            if(map.count(sum) == 0) {
                // This sum doesn't exist yet
                map[sum] = i;
            } else {
                // Check if the last index is atleast 2 spaces
                int last_index = map[sum];
                if(i - last_index >= 2) { return true; }
            }
            
        }
        
        return false;
    }
    
};
