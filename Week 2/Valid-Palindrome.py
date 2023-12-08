def isPalindrome(s: str) -> bool:
        s = s.lower()
        s1=''
        for char in s:
            if char.isalnum():
                s1+=char
        #One liner with a complexity O(1)
        return s1[:] == s1[: :-1] 

        #With a loop and complexity O(n)
        # r = len(s1)//2
        # for i in range(r):
        #     if s1[i] != s1[len(s1)-1-i]:
        #         return False
        # return True

#Both solution will give O(n time complexity because of the first for loop to filter the string)
#Both solution have space complexity of O(1)