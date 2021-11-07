class Solution {
public:
    int numberOfMatches(int n) {
        int remaining=n;
        int totalmatches=0;
        while(remaining>1)
        {
            if(remaining%2==0)
            {
                totalmatches=totalmatches+remaining/2;
                remaining=remaining/2;
            }
            else
            {
                totalmatches=totalmatches+(remaining-1)/2;
                remaining=(remaining/2)+1;
            }
        }
        return totalmatches;
    }
};
