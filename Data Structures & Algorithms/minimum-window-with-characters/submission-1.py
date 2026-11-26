from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def progress(r, l):
            while l < len(s):
                if s[l] not in chars:
                    l+=1
                else:
                    break
            if l > r:
                r = l
            return r, l

        seen = defaultdict(int)
        chars = defaultdict(int)

        for char in t:
            chars[char] += 1

        count, size = 0, len(chars)
        r, l = progress(0, 0)
        min_size = float("inf")
        res = None

        while r < len(s):
            curr = s[r]
            # if we haven't seen enough of a desired char, update count
            if curr in chars:
                if seen[curr]+1 == chars[curr]:
                    count += 1
                seen[curr] += 1

                print(curr)
                print(s[l:r+1])
                print(count, size)
                print(min_size, r-l+1)
                print(seen)
                if count == size:
                    if min_size > r-l+1:
                        min_size = r-l+1
                        res = [l, r]
                    
                    if seen[s[l]]-1 == chars[s[l]]-1:
                        count -= 1
                    seen[s[l]] -= 1
                    l += 1
                    r, l = progress(r, l)
                    if count == size and min_size > r-l+1:
                        min_size = r-l+1
                        res = [l, r]
                print(seen)
            r+=1

        while l < len(s):
            print("here", s[l:r+1])
            if seen[s[l]]-1 == chars[s[l]]-1:
                print(f"invalidated at {l}")
                break
            seen[s[l]] -= 1
            l += 1
            r, l = progress(r, l)

            if count == size and min_size > r-l+1:
                min_size = r-l+1
                res = [l, r]
                
        print(count, size)
        print(min_size, r-l+1)
        print(seen)
        return s[res[0]:res[1]+1] if res is not None else ""

            
        