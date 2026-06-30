class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {} # result map, str -> List[str]

        for str in strs:
            key = ''.join(sorted(str))
            if key not in map:
                map[key] = [str]
            else:
                map[key].append(str)
        
        return list(map.values())