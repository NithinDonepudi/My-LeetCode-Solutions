class Solution {
public:
    int maximum69Number (int num) {
        int count=0;
        int n=num,out=0;
        vector<int> nums;
        while(n>1)
        {
            int rem=n%10;
            nums.push_back(rem);
            n=n/10;
        }
        for(int i=nums.size()-1;i>=0;i--)
        {
            if(nums[i]==6 && count<1)
            {
                nums[i]=9;
                count=count+1;
            }
            out=out*10+nums[i];
        }
        return out;
    }
};
