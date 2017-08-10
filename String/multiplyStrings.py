
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        n = len(A)
        m = len(B)
        if n < m:
            A,B = B,A
            n,m = m,n

        i = m-1
        tem = []
        turn = 0
        while i>=0:
            j = n - 1
            carry = 0
            s = "0" * turn
            while j >=0:
                mul = (int(A[j]) * int(B[i])) + carry
                x = mul%10
                carry = mul/10
                s+= str(x)
                j-=1
            if carry > 0:
                s += (str(carry)[::-1])

            if len(tem) == 0:
                tem.append(s)
            else:
                s1 = tem.pop()
                ns = ""
                a = len(s1)
                b = len(s)
                if a < b:
                    s1, s = s, s1
                    a,b = b,a
                t = 0
                c = 0
                while t < b:
                    ns += str((int(s1[t]) + int(s[t]) +c)%10)
                    c  = (int(s1[t]) + int(s[t]) +c)/10
                    t +=1
                if a > b:
                    t = b
                    while t < a:
                        ns += str((int(s1[t]) + c)%10)
                        c = (int(s1[t]) + c)/10
                        t +=1
                    if c>0:
                        ns += (str(c)[::-1])
                else:
                    if c > 0:
                        ns += (str(c)[:-1])
                tem.append(ns)
            i -=1
            turn += 1
        end = len(tem[0]) - 1
        while end >=0 :
            if tem[0][end] == "0":
                end -= 1
            else:
                break
        return tem[0][end+1::-1]

a = "7737"
b = "75657"
obj = Solution()
print obj.multiply(a,b)

#290851026981985078955918627261651688832742312387314888842460711865148550965912482730570750031304678344564428861596637320

#290851027081985078955918627261751688832742312387314888842460711865148550965912482730570750031304678344564428861596637320

'02373669516882446544387640313005707503728421956905584156811229732738751472305550139999940461118963429734854230291685243'
'000000000000000000000000000000000000000000000000000000000005866811501998950267636938886642541646184361532937877704295652'