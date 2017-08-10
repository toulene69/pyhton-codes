

class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        n = len(A)
        out = []

        temp = []
        tabcount = 0
        i = 0
        while i < n:
            s = ""
            k = 0
            if A[i] == "[" or A[i] == "{":
                while k < tabcount:
                    s += "\t"
                    k+=1
                s += A[i]
                out.append(s)
                tabcount += 1
                i+=1
            elif A[i] == "]" or A[i] == "}":
                tabcount -= 1
                while k < tabcount:
                    s += "\t"
                    k+=1
                s += A[i]
                if i + 1 < n and A[i + 1] == ",":
                    s += A[i+1]
                    i += 2
                else:
                    i+=1
                out.append(s)
            else:
                j = i
                while j< n and (A[j] != "[" and A[j] != "{" and A[j] != "}" and A[j] != "]" and A[j] != ",") :
                    j+=1

                while k< tabcount:
                    s += "\t"
                    k+=1
                if A[j] == ",":
                    s += A[i:j + 1]
                    i = j + 1
                else:
                    s += A[i:j]
                    i = j

                out.append(s)
        return out
o = '["foo",{"bar":["baz",null,1.0,2]}]'
t = '{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}'
obj = Solution()
x = obj.prettyJSON(o)
for i in x:
    print i
