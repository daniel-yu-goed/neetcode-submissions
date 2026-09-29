class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # One-pass with bit mask
        # Time complexity: O(n^2)
        # Space complexity: O(n)

        """Intuition
        Every digit from 1 to 9 can be represented using a single bit in an integer.
        For example, 
            digit 1 uses bit 0,
            digit 2 uses bit 1, …,
            digit 9 uses bit 8.
        This means we can track which digits have appeared in a row, column, or 3×3 box using just one integer per row/column/box instead of a hash set.

        When we encounter a digit, we compute its bit position and check:

        if that bit is already set in the row → duplicate in row
        if that bit is already set in the column → duplicate in column
        if that bit is already set in the box → duplicate in box
        
        If none of these checks fail, we “turn on” that bit to mark the digit as seen.
        This approach is both memory efficient and fast."""

        # 1. Create three arrays of size 9:
        # rows[i] stores bits for digits seen in row i
        # cols[i] stores bits for digits seen in column i
        # squares[i] stores bits for digits seen in 3×3 box i
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        # 2. Loop through each cell (r, c) of the board:
        # Skip if the cell contains ".".
        # Convert the digit to a bit index: val = int(board[r][c]) - 1.
        # Compute the mask: mask = 1 << val.
        #   For example, digit 3 uses bit index 2
        #   its mask is: 0100
        #   we move 1 (0001) to the left for 2 spaces: 1 << 2
        #   it becomes 0100
        # if the cell value is in rows, cols, or squares --> return False
        # else: mark the digit as seen:
        # rows[r] |= mask
        # cols[c] |= mask
        # squares[(r // 3) * 3 + (c // 3)] |= mask

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                bit_index = int(board[r][c]) - 1
                mask = 1 << bit_index

                square_key = (r // 3) * 3 + (c //3)
                if mask & rows[r] or mask & cols[c] or mask & squares[square_key]:
                    return False
                rows[r] |= mask
                cols[c] |= mask
                squares[square_key] |= mask

        return True
        

    def isValidSudokuWithSet(self, board: List[List[str]]) -> bool:
        # One-pass with set
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
        