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