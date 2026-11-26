from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def ind(e):
            return ord(e)-ord("a")
        if len(s1) > len(s2):
            return False

        mp1 = [0]*26
        mp2 = [0]*26
        l = 0

        for e in s1:
            mp1[ind(e)] += 1

        for r in range(len(s2)):
            # if char is in s1
            if mp1[ind(s2[r])] > 0:
                if mp2[ind(s2[r])] < mp1[ind(s2[r])]:
                    mp2[ind(s2[r])] += 1
                    if mp1 == mp2:
                       
                        return True
                else:
                    # char frq was satified earlier, removed first occurance from left
                    while True:
                        print(s2[l:r+1])
                        
                        if s2[l] != s2[r]:
                            print(mp2)
                            mp2[ind(s2[l])] -= 1
                            print(mp2)
                            l+=1
                        else:
                            print("here")
                            l+=1
                            print(mp2)
                            break
                        
            else:
                l = r+1
                mp2 = [0]*26
        print(mp2)
        return False