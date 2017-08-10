
class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification

    # Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.
    # If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.


    def nextPermutation(self, A):
        n = len(A)
        i = n-1
        index = -1
        while i>0:
            if A[i] >A[i-1]:
                #A[i-1], A[i] = A[i] , A[i-1]
                index = i-1
                break
            i -= 1
        if index == -1:
            A.sort()
            return A
        else:

            next_min_bigger_index = index+1
            for j in range(n-1,index,-1):
                if A[j] > A[index] :
                    next_min_bigger_index = j
                    break
            A[index] , A[next_min_bigger_index] = A[next_min_bigger_index] , A[index]

            temp1 = A[:index+1]
            temp2 = A[index+1:]
            temp2.reverse()
            temp1.extend(temp2)
            return temp1

a = [4,5,3,2,1]
b = [-1,2,3]
c = [ 626, 436, 819, 100, 382, 173, 817, 581, 220, 95, 814, 660, 397, 852, 15, 532, 564, 715, 179, 872, 236, 790, 223, 379, 83, 924, 454, 846, 742, 730, 689, 112, 110, 516, 85, 149, 228, 202, 988, 212, 69, 602, 887, 445, 327, 527, 347, 906, 54, 460, 517, 376, 395, 494, 827, 448, 919, 799, 133, 879, 709, 184, 812, 514, 976, 700, 156, 568, 453, 267, 547, 8, 951, 326, 652, 772, 213, 714, 706, 972, 318, 768, 506, 59, 854, 422 ]
obj = Solution()
print obj.nextPermutation(a)

#626 436 819 100 382 173 817 581 220 95 814 660 397 852 15 532 564 715 179 872 236 790 223 379 83 924 454 846 742 730 689 112 110 516 85 149 228 202 988 212 69 602 887 445 327 527 347 906 54 460 517 376 395 494 827 448 919 799 133 879 709 184 812 514 976 700 156 568 453 267 547 8 951 326 652 772 213 714 706 972 318 768 506 854 59 422

#626 436 819 100 382 173 817 581 220 95 814 660 397 852 15 532 564 715 179 872 236 790 223 379 83 924 454 846 742 730 689 112 110 516 85 149 228 202 988 212 69 602 887 445 327 527 347 906 54 460 517 376 395 494 827 448 919 799 133 879 709 184 812 514 976 700 156 568 453 267 547 8 951 326 652 772 213 714 706 972 318 768 506 422 59 854