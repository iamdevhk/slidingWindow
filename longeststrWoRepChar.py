class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #have a list, iterate through the string if the value is not in list add it to list 
        #and make count as max of count and len of list else if the value is already in the list, 
        #get the index of the element from the list, append it to list and splice the list from 
        #the index+1of the occurance
        newst=[]
        count=0
        for i in range(0,len(s)):
            if s[i] not in newst:
                newst.append(s[i])
                count=max(count,len(newst))
            else:
                newIdx=newst.index(s[i])
                newst.append(s[i])
                newst=newst[newIdx+1:]
        return count
            
        