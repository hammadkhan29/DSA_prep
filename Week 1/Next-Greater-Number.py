def nextGreaterElement( nums1, nums2):
        res = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            if index+1 == len(nums2):
                res.append(-1)
            else:
                for j in range(index+1,len(nums2)):
                    print(j)
                    if nums2[j] > nums1[i]:
                        res.append(nums2[j])
                        break
                    elif j == len(nums2)-1:
                        res.append(-1)
                    else:
                        continue                   
        return res
    #Time complexity of O(n^2) and space complexity of O(n)