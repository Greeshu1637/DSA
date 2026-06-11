class Solution:
    def countMatches(self, items: List[List[str]], rulekey: str, rulevalue: str) -> int:
        count =0
        for i in items:
            if rulekey=="type" and i[0]==rulevalue:
                count +=1
            elif rulekey=="color" and i[1]==rulevalue:
                count +=1
            elif rulekey=="name" and i[2]==rulevalue:
                count +=1
        return count

        