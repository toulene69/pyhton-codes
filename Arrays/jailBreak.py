

def GetJumpCount(input1,input2,input3):
    """
    
    :param input1: height of jump
    :param input2: slide after jump
    :param input3: array of height of walls
    :return: min number of jumps
    """

    max_height = max(input3)
    jumps = [ -1 for _ in range(max_height + 1)]

    for i in xrange(max_height+1):
        h = i
        steps = 0
        temp = h/input1
        leftover = h % input1
        flag = False
        if temp < 1:
            jumps[i] = 1
        elif temp >= 1 :
            while temp > 0:
                if jumps[h] != -1 :
                    steps += jumps[h]
                    flag = True
                    break
                h -= input1
                if h != 0:
                    h += input2
                    temp = h / input1
                    leftover = h % input1
                else:
                    temp -= 1
                steps += 1
            if leftover > 0 and flag == False :
                steps += 1
            jumps[i] = steps
        else:
            jumps[i] = 1

    result = 0
    for wall in input3 :
        result += jumps[wall]
    print result

walls = [10]
i1 = 10
i2 = 1
GetJumpCount(i1,i2,walls)

