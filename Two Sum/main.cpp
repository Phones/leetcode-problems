#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<int> twoSum(vector<int>& nums, int target) {

    vector<int> result;    
    map<int, int> integer_list_map;

    unsigned int list_size = nums.size();
    for (int i = 0; i < list_size;i++) 
    {
      integer_list_map[nums[i]] = i;
    }

    for (int i = 0; i < list_size;i++)
    {
      int aux = target - nums[i];
      map<int,int>:: iterator it = integer_list_map.find(aux);

      if (it != integer_list_map.end())
      {
        if (i == it->second) continue;

        result.push_back(i);
        result.push_back(it->second);

        return result;
      }
    }
    return result;
  }
};
int main()
{
  int target = 10;
  vector <int> nums = {1,2,6,3,9,5,1,0};

  vector <int> result = Solution().twoSum(nums, target);

  for (auto r: result)
  {
    cout << "--> " << r << endl;
  }

}

