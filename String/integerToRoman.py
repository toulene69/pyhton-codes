

class Solution:
    # @param A : string
    # @return an integer
    def intToRoman(self, A):

        roman_dict = {1000:"m", 900:"cm", 500:"d", 400:"cd", 100:"c", 90:"xc", 50:"l", 40:"xl", 10: "x", 9:"ix", 5:"v", 4:"iv", 1:"i"}
        s = ""
        while A!=0:
            base = 0
            if A>=1000:
                base = 1000
            elif A<1000 and A>=900:
                base = 900
            elif A<900 and A>= 500:
                base = 500
            elif A<500 and A>=400:
                base = 400
            elif A<400 and A>=100:
                base = 100
            elif A< 100 and A>= 90:
                base = 90
            elif A<90 and A>=50:
                base = 50
            elif A< 50 and A>=40:
                base = 40
            elif A<40 and A>=10:
                base = 10
            elif A<10 and A>=9:
                base = 9
            elif A< 9 and A>= 5:
                base = 5
            elif A<5 and A>=4:
                base = 4
            else:
                base = 1
            r = A/base
            A= A % base
            s += roman_dict[base]*r

        s = s.upper()
        return s

x = 1231
obj = Solution()
print obj.intToRoman(x)