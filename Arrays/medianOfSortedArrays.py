

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # x1 = 0
        # y1 = len(nums1)
        # x2 = 0
        # y2 = len(nums2)
        # mid1 = 0
        # mid2 = 0
        # while x1 < y1 and x2 < y2 :
        #     mid1 = ((x1 + y1) / 2)
        #     mid2 = ((x2 + y2) / 2)
        #     if nums1[mid1] < nums2[mid2] :
        #         x1 = mid1+1
        #         y2 = mid2 - 1
        #     elif nums1[mid1] > nums2[mid2] :
        #         x2 = mid2 + 1
        #         y1 = mid1 - 1
        #     else:
        #         return nums1[mid1]
        #
        # print (nums1[mid1] + nums2[mid2])/float(2)
        print self.medianOfArrays(nums1,nums2)
        # nums = []
        # i , j = 0 ,0
        # while i < len(nums1) and j < len(nums2) :
        #     if nums1[i] <= nums2[j]:
        #         nums.append(nums1[i])
        #         i += 1
        #     else:
        #         nums.append(nums2[j])
        #         j += 1
        # if i< len(nums1):
        #     nums.extend(nums1[i:])
        # if j< len(nums2):
        #     nums.extend(nums2[j:])
        # if len(nums) %2 == 0:
        #     print (nums[len(nums)/2] + nums[len(nums)/2 - 1])/(float(2))
        # else:
        #     print (nums[len(nums) / 2 ])


    def medianOfArrays(self,A,B):
        """
        
        :param A: sorted array
        :param B: sorted array
        :return: median value
        """
        m, n = len(A), len(B)
        if m>n:
            B,A,n,m = A,B,m,n # make sure B is the array with more elements

        imin, imax, half_len = 0, m, (m+n+1)/2
        while imin <= imax:
            i = (imax + imin)/2
            j = half_len - i
            if i < m and B[j-1] > A[i] :
                imin = i+1
            elif i>0 and A[i-1] > B[j] :
                imax = i -1
            else:
                if i== 0:
                    max_left = B[j-1]
                elif j == 0:
                    max_left = A[i-1]
                else:
                    max_left = max(A[i-1], B[j-1])

                if (m+n) % 2 == 1: # for odd median is the max of the left
                    return max_left

                # for even it is the average of the max of left and min of right
                if i==m:
                    min_right = B[j]
                elif j==n:
                    min_right = A[i]
                else:
                    min_right = min(A[i],B[j])
                return (max_left + min_right)/2.0

obj = Solution()
nums1 = [1, 3]
nums2 = [2,4]
obj.findMedianSortedArrays(nums1,nums2)