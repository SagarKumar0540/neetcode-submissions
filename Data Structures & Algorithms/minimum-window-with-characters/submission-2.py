class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        target_count = {}
        for char in t :
            target_count[char] = target_count.get(char,0) + 1
        
        window_count = {}
        have,need = 0, len(target_count)

        min_len = float('inf')
        result_bounds = [-1,-1]

        left = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char,0) +1
            
            if char in target_count and window_count[char] == target_count[char]:
                have +=1
            
            while have == need : 
                current_window_len = (right - left + 1)
                if current_window_len < min_len:
                    min_len = current_window_len
                    result_bounds = [left, right]
            
                left_char = s[left]
                window_count[left_char] -=1

                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    have -=1
                
                left +=1
        
        l,r = result_bounds
        return s[l:r+1] if min_len != float("inf") else ""




