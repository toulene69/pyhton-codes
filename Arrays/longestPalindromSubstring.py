

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0]*len(s) for _ in range(len(s)+1)]
        max_pal = 1
        a = 0
        b = 0
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                max_pal ,a, b = 2 ,i, i+1
            else:
                dp[i][ i + 1] = 0
        for k in range(2,len(s) + 1):
            for i in range(len(s) - k):
                if s[i] == s[i+k] :
                    if dp[i+1][i+k-1] == 1:
                        dp[i][i+k] = 1
                        if max_pal < k+1:
                            max_pal, a, b = k+1 , i, i+k
                else:
                    dp[i][ i + k] = 0

        print s[a: b+1]


obj = Solution()
s = ""
obj.longestPalindrome(s)
