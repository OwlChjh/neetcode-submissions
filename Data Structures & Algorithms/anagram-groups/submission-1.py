class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # O(m*nlogn) time / O(mn) space
        # map = {} # result map, str -> List[str]

        # for str in strs:
        #     key = ''.join(sorted(str))
        #     if key not in map:
        #         map[key] = [str]
        #     else:
        #         map[key].append(str)
        
        # return list(map.values())
        
        groups = defaultdict(list)

        for s in strs:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord('a')] += 1

            key = tuple(cnt)
            groups[key].append(s)

        return list(groups.values())

