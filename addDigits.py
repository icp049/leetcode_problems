class Solution(object):
    def addDigits(self, num):
       
       while num >= 10: 
           next_num = 0
           while num > 0:
               next_num += num % 10
               num //=10

           num = next_num

       return num
