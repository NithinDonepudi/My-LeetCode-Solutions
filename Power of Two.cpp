class Solution {
public:
    bool isPowerOfTwo(int n) {
        while(n>=1)
        {
            if(n%2==0)
            {
                n=n/2;
            }
            else if(n%2!=0 and n==1)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        return false;
    }
};
