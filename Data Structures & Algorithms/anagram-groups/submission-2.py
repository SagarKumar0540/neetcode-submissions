from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_data = defaultdict(list)

        for str in strs:
            sorted_string = "".join(sorted(str))
            grouped_data[sorted_string].append(str)
        return list(grouped_data.values())
