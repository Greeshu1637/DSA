class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        max_num=0
        for i in s:
            count =1
            for ch in i:
                if ch ==" ":
                    count +=1
                if count > max_num:
                    max_num=count
        return max_num

        