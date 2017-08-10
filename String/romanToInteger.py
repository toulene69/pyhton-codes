

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        n = len(A)
        num = 0
        i = 0
        A = A.upper()
        rom_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        while i < n:
            if A[i] in rom_dict:
                if i+1 <n and A[i+1] in rom_dict:
                    if rom_dict[A[i]] < rom_dict[A[i+1]] :
                        num += (rom_dict[A[i+1]] - rom_dict[A[i]])
                        i+=2
                    else:
                        num += rom_dict[A[i]]
                        i+=1
                else:
                    num += rom_dict[A[i]]
                    i+=1
        return num



s = "MMMCMxCX"
obj = Solution()
print obj.romanToInt(s)




