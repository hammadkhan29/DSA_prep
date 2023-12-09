def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        len
        while i < len(nums):
            print(i, 'global')
            if nums[i] == 0:
                print('at 0' , i)
                nums.append(nums[i])
                nums.remove(nums[i])
                if (i!=len(nums)-1) and (nums[i+1] != 0):
                    i+=1
                elif nums[len(nums)-1] == 0:
                    i+=1
                else:
                    continue
            else:
                i+=1
