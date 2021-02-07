class Solution(object):
    def largestAltitude(self, gain): {
    public int[] ConstructArray(int n, int k) {
        var result = new int[n];
        int left=1, right=n;
        for(int i=0; i<n; i++){
            result[i] = k%2 !=0 ? left++ : right--;
            if(k>1){
                k--;
            }                
        }
                
        return result; 
    }
}
