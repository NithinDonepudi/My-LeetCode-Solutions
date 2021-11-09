class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int> answer;
        for(int i=0;i<boxes.length();i++)
        {
            answer.push_back(0);
            for(int j=0;j<boxes.length();j++)
            {
                 if(boxes[j]=='1')
                 {
                    answer[i]=answer[i]+abs(i-j);
                 }
            }
        }
        return answer;
    }
};
