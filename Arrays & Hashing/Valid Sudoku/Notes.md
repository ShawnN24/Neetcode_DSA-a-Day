# Valid Sudoku

## Problem Statement
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

1. Each row must contain the digits 1-9 without duplicates.
2. Each column must contain the digits 1-9 without duplicates.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

### Example 1:

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true

### Example 2:

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false

## My Solution Journey

Approach 1: Brute Force
The obvious first approach would be to brute force the question by looping through the entire list to verify row, col, and square
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".": 
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
            
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
```
Time & Space Complexity
- Time complexity: O(n^2)
- - Loop through a full list O(n^2) three times
- Space complexity: O(n^2)
- - We store the set seen for the full list

Approach 2: Hash Set (One Pass)
The best approach is to loop through the list once verifying if there are any duplicates for row, col, and square (subbox)
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardColumn = [[] for _ in range(len(board))]
        boardSubbox = defaultdict(set) #mapping {subbox index: set of values}
        
        for i in range(len(board)):
            row = board[i]
            tempSet = set()
            for j in range(len(row)):
                box = row[j]
                subbox = math.floor(i / 3) * 3 + math.floor(j / 3)
                if box == ".":
                    continue
                if (int(box) in tempSet
                or int(box) in boardColumn[j]
                or int(box) in boardSubbox[subbox]):
                    return False
                tempSet.add(int(box))
                boardColumn[j].append(int(box))
                boardSubbox[subbox].add(int(box))
        return True
```
Time & Space Complexity
- Time complexity: O(n^2)
- - Loop through a full list O(n^2) once
- Space complexity: O(n^2)
- - We store the set seen for the full list

## Time 
07/06/2025 | 1:06:09