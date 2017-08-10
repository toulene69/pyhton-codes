


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        lenght of longest substring without repeating characters
        "abcabcbb", the answer is "abc"
        :type s: str
        :rtype: int
        """
        dp = {}
        sub = 0
        j=0
        for i in range(len(s)):
           if s[i] in dp:
               j = max(j,dp[s[i]] + 1)
           dp[s[i]] = i
           sub = max(sub,i-j+1)
        print sub

    def checkLongestSubstring(self,s,i,j,dp):
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        if (i,j) in dp:
            return dp[(i,j)]
        else:
            sub = len(s)
            dp[(i, j)] = sub
            for x in s:
                count = 0
                for y in s:
                    if x==y:
                        count += 1
                if count > 1:
                    sub = -1
                    del(dp[i,j])
                    break

            return max(sub,self.checkLongestSubstring(s[i+1:j],i+1,j,dp),self.checkLongestSubstring(s[i:j-1],i,j-1,dp))


obj = Solution()
obj.lengthOfLongestSubstring("abcabcbba")