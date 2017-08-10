class Solution:
    # @param arrive : list of integers "arrival dates"
    # @param depart : list of integers "departure dates"
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        if K == 0:
            return False
        n = len(arrive)
        if n <= K:
            return True
        arrive.sort()
        depart.sort()
        count = 0
        i , j = 0, 0
        flag = True
        while i<n and j<n:
            if arrive[i] < depart[j] :
                count += 1
                i += 1
            elif arrive[i] > depart[j] :
                count -= 1
                j += 1
            else:
                i += 1
                j += 1

            if count > K :
                flag = False
                break

        return flag

a = [2, 1 ,5, 4]
d = [10, 3, 7, 6]
k =3
obj = Solution()
print obj.hotel(a,d,k)