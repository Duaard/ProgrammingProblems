class Solution {
public:
    bool canJump(vector<int>& nums) {
        const int n = nums.size();
        int highest_index = 0;
        
        for(int i = 0; i < n; i++) {
            if(i > highest_index) {
                return false;
            }
            highest_index = max(highest_index, nums[i] + i);
        }
        
        return true;
    }
};
