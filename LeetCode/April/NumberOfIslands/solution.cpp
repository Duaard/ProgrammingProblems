class Solution {
public:
    class FindUnion {
        private:
            vector<int> id;
            vector<int> size;
            int subsets;
        public:
            FindUnion(int n) {
                // Initialize the size and id array
                size = vector<int>(n);
                for(int i = 0; i < n; i++) {
                    id.push_back(i);
                }
                
                subsets = n;
            }
        
            int getSubsets() {
                return subsets;
            }
        
            int root(int i) {
                int x = i;
                while(x != id[x]) {
                    x = id[x];
                }
                
                return x;
            }
        
            bool connected(int p, int q) {
                return root(p) == root(q);
            }
        
            void connect(int p, int q) {
                // cout << "Connecting " << p << " and " << q << "\n";
                int i = root(p);
                int j = root(q);
                if (i == j) return;
                if (size[i] < size[j]) {
                    id[i] = j;
                    size[j] += size[i];
                } else {
                    id[j] = i;
                    size[i] += size[j];
                }
                subsets--;
            }
        
            void decSubsets() {
                subsets--;
            }
        
            void showID() {
                for(int i = 0; i < id.size(); i++) {
                    cout << "ID of " << i << " is " << id[i] << "\n";
                }
            }
        
            
    };
    
    bool withinRange(int i, int n) {
        if (i < 0) {
            return false;
        }
        if (i > n - 1) {
            return false;
        }
        
        return true;
    }   
    
    int numIslands(vector<vector<char>>& grid) {
        // Easier to visualize grid as a 1d array
        // 1 1
        const int r = grid.size();
        const int c = r > 0 ? grid[r-1].size() : 0;
        const int n = r * c;
        vector<int>nums;
        for(int i = 0; i < n; i++) {
            int row = i / c; 
            int col = i % c;
            int x = grid[row][col] == '1' ? 1 : 0;
            nums.push_back(x);
        }
        // Create FindUnion object for handling dynamic connectivity
        FindUnion fu(n);
        // Loop through array to fill up connections
        for(int i = 0; i < n; i++) {
            // Check four directions for connections
            if(nums[i] == 1) {
                // Top i - c
                if(withinRange(i-c, n) && nums[i-c] == 1) {
                    fu.connect(i,i-c);
                }
                // Bottom i + =c
                if(withinRange(i+c, n) && nums[i+c] == 1) {
                    fu.connect(i, i+c);
                }

                // Left -1
                if(withinRange(i-1, n) && i % c != 0 && nums[i-1] == 1) {
                    fu.connect(i, i-1);
                }
                // Right +1
                if(withinRange(i+1, n) && i % c != c-1 && nums[i+1] == 1) {
                    fu.connect(i, i+1);
                }
            } else {
                // Value of tile is 0
                // Decrease the number of subset
                fu.decSubsets();
            }
        }
        
        // Return the number of subsets
        return fu.getSubsets();
    }
};
