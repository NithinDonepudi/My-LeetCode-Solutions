class Solution {
public:
    void reverseString(vector<char>& s) {
        for(int i=0;i<s.size()/2;i++)
        {
            int temp;
            temp=s[s.size()-1-i];
            s[s.size()-1-i]=s[i];
            s[i]=temp;
        }
    }
};
