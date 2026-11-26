class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # keep invariant that s should be the shortest
        if n < m:
            s, t = t, s
            n, m = m, n

        # if length differes by more than 2, 1-edit distance impossible
        if n-m > 1:
            return False

        edited = False
        i=j=0

        while i < m and j<n:
            # same, advance both
            if s[i] == t[j]:
                i+=1
                j+=1
                continue
            
            # if sencond edit, return false
            if edited:
                return False
            # mark first edit
            edited = True

            # if same length, this must be a replace operation
            # inserting or deleting, would lead to multiple operations
            if m==n:
                i+=1
                j+=1
            # m<n, insert. only j advances
            else:
                j+=1

        return edited or (n == m+1)