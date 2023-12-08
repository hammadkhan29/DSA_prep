def validPalindrome( s: str) -> bool:
        def is_palindrome_range(i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j))

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Check if removing either s[left] or s[right] results in a palindrome
                return is_palindrome_range(left, right - 1) or is_palindrome_range(left + 1, right)
            left += 1
            right -= 1

    # The string is already a palindrome or can be made a palindrome by removing at most one character
        return True

