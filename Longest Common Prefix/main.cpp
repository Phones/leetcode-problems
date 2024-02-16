#include <bits/stdc++.h>
using namespace std;


class Solution {
  public:
    string longestCommonPrefix(vector<string>& strs) {
        string first_str = strs[0], result = "";
        for (int i = 0; i < first_str.size(); i++)
        {
            for(auto str_: strs)
            {
                if (i >= str_.size() || str_[i] != first_str[i])
                {
                    return result;
                }
            }
            result += first_str[i];
        }
        return result;
    }
};


int main()
{
    Solution solution;
    vector <string> teste = {"flower","flow","flight"};
    cout << solution.longestCommonPrefix(teste) << endl; 
    
    teste = {"dog","racecar","car"};
    cout << solution.longestCommonPrefix(teste) << endl; 
    
    teste = {"a"};
    cout << solution.longestCommonPrefix(teste) << endl; 
}
