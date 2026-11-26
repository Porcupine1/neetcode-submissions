from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        d = deque([])
        maxSeen, count = 0, 0
        l, r = 0, 0
        
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                d.append(s[r])
                count += 1
                maxSeen = max(maxSeen, count)
            
            else:
                while d:
                    curr = d.popleft()
                    seen.remove(curr)
                    if curr == s[r]:
                        d.append(s[r])
                        seen.add(s[r])
                        break

                count = len(d)
            r += 1
            print(d)

        return maxSeen