def numUniqueEmails(self, emails) -> int:
        res = {}
        for i in emails:
            new_mail = i.split('@')[1]
            email = ''
            for j in i:
                if j == '.':
                    continue
                elif (j == '+') or (j=='@'):
                    break
                else:
                    email+=j
            res[email+'@'+new_mail]= i
        print(res)
        return len(res)
#Time complexity is O(n^2) because of nested loops
#Space complexity is m*n where m is length of email address and n is total number of email address
