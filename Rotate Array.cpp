class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> ans;
        k=k%nums.size();
        for(int i=0;i<nums.size();i++)
        {
            ans.push_back(nums[(nums.size()-k+i)%(nums.size())]);
        }
        nums=ans;
    }
};
