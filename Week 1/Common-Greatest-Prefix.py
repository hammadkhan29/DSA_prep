def longestCommonPrefix(strs) -> str:
        reference = strs[0]
        ref = []
        prefix = ''
        if len(strs) == 1:
            return strs[0]
        for i in range(1,len(strs)):
            pre = ''
            j = 0
            while j < min(len(reference),len(strs[i])):
                if reference[j] != strs[i][j]:
                    break
                else:
                    pre+=reference[j]
                j+=1
            prefix = pre
            ref.append(prefix)
        ref.sort()
        return ref[0]
#TC is n^m and space is also same