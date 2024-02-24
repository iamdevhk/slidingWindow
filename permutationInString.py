from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #get a dictionary of all values in s1, basically counter, then set l=0 , r=len(s1)
        #while r <= length of s2, check if counte rof s1 and counter of s2[l:r] is same, if same return true
        #else increase left and right pointers by 1 and if it goe sout while loop return false
        d=Counter(s1)
        l=0
        r=len(s1)
        while r<=len(s2):
            
            if d==Counter(s2[l:r]):
                return True
            else:
                l+=1
                r+=1
        return False
        