def containsDuplicate( nums) -> bool:
        # res = []
        # for i in range(len(nums)):
        #     if nums[i] in res:
        #         return True
        #     res.append(nums[i])
        # return False
#Time complexity is O(n^2) because in nums take tc of O(n)
#so total tc is O(n^2)

# But in dict and set lookups take O(1) tc 
#space complexity is O(n) in both cases
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = True

        return False
