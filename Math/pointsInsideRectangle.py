class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @return an integer
    def solve(self, A, B, C, D):
        n = len(C)
        count = 0
        # for i in xrange(n):
        #     s1 = self.pointPosition(C[i],D[i],A[0],B[0],A[1],B[1])
        #     s2 = self.pointPosition(C[i], D[i], A[1], B[1], A[2], B[2])
        #     s3 = self.pointPosition(C[i], D[i], A[2], B[2], A[3], B[3])
        #     s4 = self.pointPosition(C[i], D[i], A[3], B[3], A[0], B[0])
        #     if (s1+s2+s3+s4) == -4 or (s1+s2+s3+s4) == 4:
        #         count+=1
        arRec = self.areaOfTriangle(A[0],B[0],A[1],B[1],A[2],B[2]) + self.areaOfTriangle(A[2],B[2],A[3],B[3],A[0],B[0])
        for i in xrange(n):
            s1 = self.areaOfTriangle(C[i],D[i],A[0],B[0],A[1],B[1])
            s2 = self.areaOfTriangle(C[i], D[i], A[1], B[1], A[2], B[2])
            s3 = self.areaOfTriangle(C[i], D[i], A[2], B[2], A[3], B[3])
            s4 = self.areaOfTriangle(C[i], D[i], A[3], B[3], A[0], B[0])
            if s1==0 or s2==0 or s3==0 or s4==0:
                continue
            arS = s1+s2+s3+s4
            if arRec == arS:
                count += 1

        return count

    def areaOFRectangle(self,x1,y1,x2,y2,x3,y3):
        area = (((x2-x1)**2 + (y2-y1)**2) * ((x3-x2)**2 + (y3-y2)**2))**0.5
        return area


    def pointPosition(self,px,py,x1,y1,x2,y2):
        val = ( ((px - x1)*(y2-y1)) - ((py-y1)*(x2-x1)) )
        if val <0:
            return -1
        elif val > 0:
            return 1
        else:
            return 0
    def areaOfTriangle(self,x1,y1,x2,y2,x3,y3):
        area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2.0)
        return area

# a = [0,-2,2,4]
# b = [0,2,6,4]
# c = [1,2,1,5,-3]
# d = [3,4,2,5,1]
A = [ 757806, 870553, 1208794, 1096047 ]
B = [ 750581, 637834, 976075, 1088822 ]
C = [ -960840, -955568, -948123, -944567, -932689, -909006, -899213, -872499, -816231, -815487, -745458, -733965, -731767, -724160, -674483, -668124, -638622, -626199, -601653, -558231, -555957, -545997, -544386, -543614, -535798, -534548, -515867, -476700, -475144, -469624, -458175, -438328, -417182, -381407, -371638, -337506, -329494, -310312, -294120, -293259, -286345, -239709, -236737, -226459, -101763, -95015, -92985, -45365, -39041, -16265, 14345, 20699, 43223, 59858, 80467, 155882, 178162, 185280, 219005, 232976, 270563, 279358, 282342, 289593, 290780, 317859, 329292, 341423, 361695, 393776, 422139, 433328, 444707, 470220, 508399, 509636, 516573, 532007, 537797, 541645, 542654, 606489, 609080, 614672, 617072, 619918, 626655, 690373, 721697, 723175, 750776, 763166, 771255, 814811, 829093, 887413, 898447, 908990, 923037, 935731 ]
D = [ -567401, -305898, -133127, 306804, -128699, 994624, -618554, -827823, 67682, 259449, 256638, 675439, 866179, 202790, -859640, -46451, -328534, 750143, 256970, -520372, -873728, 298573, -830382, 539967, -142881, 886848, -43491, -1859, -229702, 300055, 848590, -694308, -545489, 779474, 916511, -624980, 677863, 377492, 341491, -486602, 414689, 760790, 740840, -294549, -257631, -180968, -361856, -703029, -309178, -15868, -881165, 339541, -137928, -453872, -68725, -569599, -504392, 997206, -545062, 145377, -865567, 666039, -194872, 436167, 835283, -168730, 877227, 663200, -7680, -368684, -566371, 497670, -258796, 29626, -969593, 30447, -419927, -205084, -428907, -854872, 327835, -75951, -465094, -474657, 805466, 874210, 473763, -956825, -188138, -425076, -899816, 588745, -56595, 342698, 305541, 610272, -930175, 175954, 735343, 679916 ]
obj = Solution()
print obj.solve(A,B,C,D)
# print obj.solve(a,b,c,d)