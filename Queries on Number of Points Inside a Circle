class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int> answer;
        int count;
        for(int j=0;j<queries.size();j++)
        {
            count=0;
            for(int i=0;i<points.size();i++)
            {
                if(pow(queries[j][0]-points[i][0],2)+pow(queries[j][1]-points[i][1],2)<=pow(queries[j][2],2))
                {
                    count++;
                }
            }
            answer.push_back(count);
        }
        return answer;
    }
};
