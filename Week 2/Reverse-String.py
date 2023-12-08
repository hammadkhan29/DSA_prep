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

