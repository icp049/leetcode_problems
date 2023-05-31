class Solution {
    public:

    bool isPalindrome(int x){
        int oldNumber = x;
        long long int newNumber = 0;

      while(0<x){
          int temp = x%10;
          newNumber = newNumber*10+temp;
          x = x/10;
      }

      if(oldNumber == newNumber){
          return true;
      } else{
          return false;
      }

    }
};
