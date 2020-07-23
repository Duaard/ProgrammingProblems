class Solution {
public:
    bool checkValidString(string s) {
        vector<int> left;
        vector<int> special;
        int i = 0;
        for(char c : s) {
            if(c == ')') {
                if (left.size() > 0) {
                    // Pop left
                    left.pop_back();
                } else if (special.size() > 0) {
                    // Use special char
                    special.pop_back();     
                } else {
                    return false;
                }
            } else if (c == '(') {
                left.push_back(i);
            } else {
                // Special char '*'
                special.push_back(i);
            }
            i++;
        }
        if(left.size() > special.size()) {
            return false;
        }
        for(int i = left.size()-1; i >= 0; i--) {
            if(left[i] > special.back()) {
                return false;
            }
            special.pop_back();
        }
        return true;
    }
};
