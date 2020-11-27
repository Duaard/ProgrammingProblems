class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        const int n = nums1.size(), m = nums2.size();
        int min_index, max_index, i, j;
        min_index = 0;
        max_index = min(n, m);
        int max_A, max_B, min_A, min_B;
        const vector<int> a = n < m ? nums1 : nums2;
        const vector<int> b = a == nums1 ? nums2 : nums1;

        while (min_index <= max_index)
        {
            i = (max_index + min_index) / 2;
            j = ((n + m + 1) / 2) - i;

            // printf("min: %i, max: %i\ni: %i, j: %i\n", min_index, max_index, i, j);

            // 1 2 3 4 b
            // 5 6 7 8 a
            //
            max_A = i > 0 ? a[i - 1] : INT_MIN;
            max_B = j > 0 ? b[j - 1] : INT_MIN;
            min_A = i < min(n, m) ? a[i] : INT_MAX;
            min_B = j < max(n, m) ? b[j] : INT_MAX;
            // printf("First Part: A= %i, B= %i\n", max_A, max_B);
            // printf("Last Part: A= %i, B= %i\n", min_A, min_B);

            // if (j < 0)
            // {
            //     max_index = i - 1;
            //     continue;
            // }

            // Last of A_1 is greater than First of B_2
            if (max_A > min_B)
            {
                // Decrease max
                max_index--;
                continue;
            }
            // Last of B_1 is greater than First of A_2
            else if (max_B > min_A)
            {
                // Increase min
                min_index++;
                continue;
            }
            else
            {
                // Found the right partition
                // Handle edge cases here

                break;
            }
        }

        double ans = (n + m) % 2 != 0 ? max(max_A, max_B) : (max(max_A, max_B) + min(min_A, min_B)) / 2.0;
        return ans;
    }
};