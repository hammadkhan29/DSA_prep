def majorityElement( nums) -> int:
        element = {}
        for i in range(len(nums)):
            if nums[i] in element:
                element[nums[i]] += 1
            else:
                element[nums[i]] = 1
        print(element)
        
        max_key = max(element, key=element.get)
        print(max_key)
        return max_key
#Time and Space complexity of O(n)