class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r, row in enumerate(board):
            for c, value in enumerate(row):
                # Skip empty spaces
                if value == ".":
                    continue
                # Check columns
                if value in cols[c]:
                    return False
                else:
                    cols[c].add(value)
                # Check rows
                if value in rows[r]:
                    return False
                else:
                    rows[r].add(value)
                # Check squares
                square = (r // 3, c // 3)
                if value in squares[square]:
                    return False
                else:
                    squares[square].add(value)
        return True
