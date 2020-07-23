class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 0) return -1;

        int lo = 0, hi = n-1;
        int first = nums[0];
        while(lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int val = nums[mid];
            if(val == target) {
                return mid;
            }
            
            bool m_big = val >= first;
            bool t_big = target >= first;
            // If target and mid is in the same 'set'
            if(m_big == t_big) {
                // Perform normal binary search
                if(target > val) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            } else {
                // Target and mid is in different 'sets'
                if(m_big) {
                    // Target is smaller than first, go right
                    lo = mid + 1;
                } else {
                    // Query is smaller than first, go left
                    hi = mid - 1;
                }
            }
        }
        
        // Not found
        return -1;
    }
};
