def twoSum( nums, target: int) :
      result = []
      ref_dict ={}

      for i , num in enumerate(nums):

        diff = target - num

        if diff in ref_dict :
            result.append(ref_dict[diff])
            result.append(i)
            return result

        ref_dict[num] = i

      return result
# O(n) is time and space complexity