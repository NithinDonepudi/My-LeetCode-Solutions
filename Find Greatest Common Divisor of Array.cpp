class Solution {
public:
    int findGCD(vector<int>& nums) {
        int GCD=1;
        int n=nums.size();
        sort(nums.begin(),nums.end());
        GCD=gcd(nums[0],nums[n-1]);
        return GCD;
    }
};
