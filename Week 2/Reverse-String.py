def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #using loop
        s1 = ''.join(s)
        for i in range(len(s1)):
            s[i] =s1[len(s1)-i-1]
        print(s)

        #Direct using built in method
        #s.reverse()
        left, right = 0, len(s) - 1

    # Swap characters from the beginning and end until the pointers meet
        while left < right:
        # Swap characters
            s[left], s[right] = s[right], s[left]

        # Move pointers towards the center
            left += 1
            right -= 1
        print(s)
#Time complexity is O(n)
