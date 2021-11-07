class Solution {
public:
    int minOperations(int n) {
        int arr[n],sum=0,mean,noop=0;
        for(int i=0;i<n;i++)
        {
            arr[i]=(2*i)+1;
            sum=sum+arr[i];
        }
        mean=sum/n;
        for(int i=0;i<n/2;i++)
        {
            noop=noop+abs(arr[i]-mean);
        }
        return noop;
    }
};
