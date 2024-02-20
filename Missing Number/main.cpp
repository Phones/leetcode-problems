#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        return ((n * (n + 1)) / 2) - std::accumulate(nums.begin(), nums.end(), 0);
    }
};

int main()
{
    vector <int> teste = {0,1};
    cout << Solution().missingNumber(teste) << endl;
}