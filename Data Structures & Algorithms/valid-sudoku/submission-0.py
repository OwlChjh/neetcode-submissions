class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        hashset = set()

        for i in range(n):
            for j in range(n):
                ch = board[i][j]
                if ch != '.':
                    row_key = ch + 'in row ' + str(i)
                    col_key = ch + 'in col ' + str(j)
                    block_key = ch + 'in block ' + str(i//3) + ' and '+ str(j//3)
                    if row_key in hashset or col_key in hashset or block_key in hashset:
                        return False
                    hashset.add(row_key)
                    hashset.add(col_key)
                    hashset.add(block_key)

        return True