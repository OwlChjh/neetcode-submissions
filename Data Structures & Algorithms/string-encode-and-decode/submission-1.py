class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)
        # ['leet', 'code']
        # 4#leet4#code
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the position of the delimiter
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # Extract length
            j += 1  # Skip the '#'
            res.append(s[j:j+length])
            i = j + length  # Move to the next segment
        return res