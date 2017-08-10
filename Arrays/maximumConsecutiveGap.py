import sys
class Solution:
    # @param A : tuple of integers
    # @return an integer
    #Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
    def maximumGap(self, A):
        n = len(A)
        if n < 2:
            return 0

        maxItem = max(A)
        minItem = min(A)
        gap = (maxItem - minItem)/(n-1) + 1
        bucketMin = [sys.maxint for i in range(n)]
        bucketMax = [-sys.maxint-1 for i in range(n)]

        for i in range(n):
            if A[i] != maxItem and A[i] != minItem :
                item = A[i]
                bucket_index = (item - minItem)/ gap
                bucketMin[bucket_index] = min(bucketMin[bucket_index],item)
                bucketMax[bucket_index] = max(bucketMin[bucket_index],item)

        maxGap = -sys.maxint-1
        previous = minItem
        for i in range(n):
            if bucketMin[i] == sys.maxint and bucketMax[i] == -sys.maxint-1:
                continue
            maxGap = max(maxGap, bucketMin[i] - previous)
            previous = bucketMax[i]
        maxGap = max(maxGap, maxItem - previous)
        return maxGap


a = (1, 10)
obj = Solution()
print obj.maximumGap(a)