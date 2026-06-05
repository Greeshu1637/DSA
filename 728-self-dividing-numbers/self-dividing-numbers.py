class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1):
            num=i
            flag=True
            while num>0:
                digit = num %10
                if digit ==0 or i% digit !=0:
                    flag = False
                    break
                num //=10
            if flag:
                ans.append(i)
                
        return ans            

              