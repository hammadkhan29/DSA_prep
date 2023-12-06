def isAnagram(s: str, t: str) -> bool:
        # Inefficient solution with more runtime and memory usage

        # if len(s) != len(t):
        #     return False

        # s = [val for val in s]
        # t = [val for val in t]

        # s.sort()
        # t.sort()

        # if s == t:
        #     return True

        # return False
        #Time Compleixty is nlog(n) and space is O(n)

        #A bt better than previous version with better runtime

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)

        # return sorted_s == sorted_t
        #Time Compleixty is nlog(n) and space is O(n)


        #This version has a better time complexity and space complexity
        if len(s) != len(t):
            return False

        char_count = [0] * 26

        for char in s:
            char_count[ord(char) - ord('a')] += 1

        for char in t:
            char_count[ord(char) - ord('a')] -= 1
            if char_count[ord(char) - ord('a')] < 0:
                return False

        return all(count == 0 for count in char_count)
        #Time Compleixty is O(n) and space is O(1)

s = input('Enter First String')
t = input('Enter Second String')

answer = isAnagram(s,t)
print(answer)