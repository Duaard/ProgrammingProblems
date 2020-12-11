class Solution
{
public:
    // Create a map of roman nums
    vector<string> rom = {"I", "V", "X", "L", "C", "D", "M"};
    vector<int> val = {1, 5, 10, 50, 100, 500, 1000};
    string intToRoman(int num)
    {
        unordered_map<int, string> intToRom;

        for (int i = 0; i < val.size(); i++)
        {
            intToRom[val[i]] = rom[i];
        }
        int place = 0;
        string ans = "";
        while (num)
        {
            int d = num % 10;
            num /= 10;
            int p = (int)pow(10, place);
            place++;

            if (d == 9)
            {
                ans = intToRom[p] + intToRom[p * 10] + ans;
            }
            else if (d == 4)
            {
                ans = intToRom[p] + intToRom[p * 5] + ans;
            }
            else
            {
                for (int i = 0; i < d % 5; i++)
                    ans = intToRom[p] + ans;
                if (d >= 5)
                    ans = intToRom[p * 5] + ans;
            }
        }
        return ans;
    }
};