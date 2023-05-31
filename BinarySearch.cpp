class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;

        while(left <= right){
            int middle = left+(right-left)/2;
            int match = nums[middle];
          
          if (target == match){
              return middle;
          } else if(target < match){
            right = middle -1;
          } else {
              left = middle + 1;
          }
        }
        return -1;
    }
};
