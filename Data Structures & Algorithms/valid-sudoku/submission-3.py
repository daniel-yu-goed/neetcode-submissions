class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time complexity: O(n^2)
        # Space complexity: O(n^2)
        
        # 1. Create three hash maps of sets:
        # rows to track digits in each row
        # cols to track digits in each column
        # squares to track digits in each 3×3 sub-box, keyed by (r // 3, c // 3)
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # 2. Loop through every cell in the board:
        # if the cell value is in rows, cols, or squares --> return False
        # else: add the digit to all three sets
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                # special case
                if value == ".":
                    continue

                square_key = (r // 3, c // 3)
                if value in rows[r] or value in cols[c] or value in squares[square_key]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                squares[square_key].add(value)
        # 3. If all rows, columns, and 3×3 boxes pass these checks without duplicates,
        # return true.
        return True
        