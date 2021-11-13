// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int start = 1, end = n;
        long long int mid = 1;

        while(start < end) {
            mid = start + (end - start) / 2;
            bool ans = isBadVersion(mid);
            if(ans == false) {
                start = mid + 1;
            }
            else if(ans == true) {
                end = mid - 1;
            }
        }
        if(isBadVersion(start)) {
            return start;
        }
        return start+1;  
    }
};
