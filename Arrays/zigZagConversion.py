

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        # if numRows == 2:

        i = numRows
        count = n = len(s)
        verticals = []
        zigs = []
        j=0
        isVertical = True
        start = 0
        end = i-1
        while count>0 :
            temp = []
            if isVertical :
                for k in range(start,end + 1):
                    if k < n:
                        temp.append(s[k])
                        count -= 1
                    else:
                        break
                temp.reverse()
                verticals.append(temp)
                isVertical = False
                start = end + 1
                end = end + i - 1
            else:
                for k in range(start,end):
                    if k < n:
                        temp.append(s[k])
                        count -= 1
                    else:
                        break
                zigs.append(temp)
                isVertical = True
                start = end
                end = end + i - 1

        print verticals
        print zigs
        str = ""
        m = len(verticals) + len(zigs)
        zigtot = i - 2
        for x in range(numRows + 1):
            if x > 0:
                iv = 0
                iz = 0
                for y in range(m):
                    if y % 2 == 0 :
                        if iv < len(verticals) and len(verticals[iv]) != 0:
                            str += verticals[iv].pop()
                            iv += 1
                    else :
                        if iz < len(zigs) and len(zigs[iz]) != 0 and len(zigs[iz]) == zigtot - x + 1:
                            str += zigs[iz].pop()
                            iz += 1
            else:
                for items in verticals:
                    str += items.pop()
        print str
obj = Solution()
s = "abcdefghijk"
rows = 4
obj.convert(s,rows)


