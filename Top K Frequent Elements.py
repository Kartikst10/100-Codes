# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list)
        for s in strs:
            count = [0] *26
            for c in s:
                count[ord(c) - ord("a")] +=1
            hashset[tuple(count)].append(s)
            print(count)
        return hashset.values()