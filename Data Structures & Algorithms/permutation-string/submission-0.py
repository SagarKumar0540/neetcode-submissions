from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_char_count = {}
        s2_char_count = {}
        max_len = len(s1)
        left = 0

        for char in s1:
            s1_char_count[char] = s1_char_count.get(char, 0) + 1
        
        for right in range(len(s2)):
            s2_char_count[s2[right]] = s2_char_count.get(s2[right], 0) + 1

            while (right-left+1) > max_len:
                if s2[left] in s2_char_count:
                    s2_char_count[s2[left]] -=1
                    if s2_char_count[s2[left]] == 0:
                        del s2_char_count[s2[left]]
                left +=1
            
            if (right-left +1) == max_len:
                if s1_char_count == s2_char_count:
                    return True
        
        return False
            






