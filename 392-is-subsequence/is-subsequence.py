class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      
        # for i in range(0,len(s)):
        #     ans = False 
        #     for j in range(0,len(t)):
        #         if s[i] == t[j]:
        #             ans = True
        #             break
        #     if ans == False:
        #         return False
        # return True
                
        j = 0

        for i in range(len(s)):
            ans = False

            while j < len(t):
                if s[i] == t[j]:
                    ans = True
                    j += 1
                    break
                j += 1

            if ans == False:
                return False

        return True
                    
        
        
        
        
        
        
        
        # i,j=0,0
        # while i <len(s) and j<len(t):
        #     if s[i]==t[j]:
        #         i+=1
        #     j+=1
        # return True if i == len(s) else False
        