from time import time
class Puzzle:
    choices = [i for i in range(1,10)]
    choices2 = set([i for i in range(0,10)])
    empty_board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]

    def __init__(self, board=empty_board):
        self.board = board
        self.attempts = 0

    def find_next_empty(self):
        for row_idx, row in enumerate(self.board):
            for col_idx, col in enumerate(row):
                if col == 0:
                    return row_idx, col_idx
        return 81,81

    def get_value(self, row_idx, col_idx):
        return self.board[row_idx][col_idx]

    def get_row(self, row_idx):
        return self.board[row_idx]

    def get_col(self, col_idx):
        return [row[col_idx] for row in self.board]

    def get_box(self, row_idx, col_idx):
        box = []
        row_start = (row_idx // 3) * 3
        col_start = (col_idx // 3) * 3
        for _row in self.board[row_start: row_start + 3]:
            for _col in _row[col_start: col_start + 3]:
                box.append(_col)
        return box

    def check_row(self, row_idx, value):
        row = self.get_row(row_idx)
        return value in row

    def check_col(self, col_idx, value):
        col = self.get_col(col_idx)
        return value in col

    def check_box(self, row_idx, col_idx, value):
        box = self.get_box(row_idx, col_idx)
        return value in box

    def is_valid(self, row_idx, col_idx, value):
        if self.check_row(row_idx, value) or self.check_col(col_idx, value) or self.check_box(row_idx, col_idx, value):
            return False
        return True

    def get_choices(self, row_idx, col_idx):
        row, col, box = self.get_row(row_idx), self.get_col(col_idx), self.get_box(row_idx, col_idx)
        intersection = set(row).intersection(col, box)
        return Puzzle.choices2.difference(intersection)


    def solve_regular(self):
        r, c = self.find_next_empty()
        self.attempts += 1
        if r == 81:
            print(f"Took {self.attempts} tries to solve.\n{self}")
            return True
        
        for choice in Puzzle.choices:
            if self.is_valid(r, c, choice):
                self.board[r][c] = choice
                if self.solve_regular():
                    return True
            self.board[r][c] = 0
        return False

    def solve_optimized(self):
        r, c = self.find_next_empty()
        self.attempts += 1
        if r == 81:
            print(f"Took {self.attempts} tries to solve.\n{self}")
            return True
        
        for choice in self.get_choices(r,c):
            if self.is_valid(r, c, choice):
                self.board[r][c] = choice
                if self.solve_optimized():
                    return True
            self.board[r][c] = 0
        return False
        
    def __str__(self):
        printed_board = ""
        for row_idx, row in enumerate(self.board):
            if row_idx%3 == 0 and row_idx != 0:
                printed_board += "- - - + - - - + - - -\n"
            for col_idx, col in enumerate(row):
                if col_idx%3==0 and col_idx != 0:
                    printed_board += "| "
                printed_board += str(col) + " "
            printed_board += "\n"
        return printed_board
            
        
if __name__ == "__main__":
    # a = Puzzle()
    # print(a)

    # example_puzzle = [
    #     [3,9,0,0,5,0,0,0,0],
    #     [0,0,0,2,0,0,0,0,5],
    #     [0,0,0,7,1,9,0,8,0],
    #     [0,5,0,0,6,8,0,0,0],
    #     [2,0,6,0,0,3,0,0,0],
    #     [0,0,0,0,0,0,0,0,4],
    #     [5,0,0,0,0,0,0,0,0],
    #     [6,7,0,1,0,5,0,4,0],
    #     [1,0,9,0,0,0,2,0,0]
    # ]
    # example = Puzzle(example_puzzle)
    # start1 = time()
    # example.solve_regular()
    # end1 = time()

    # example2 = Puzzle(example_puzzle)
    # start2 = time()
    # example2.solve_optimized()
    # end2 = time()
    
    # print(f"Regular Solve: {end1 - start1}s")
    # print(f"Optimized Solve: {end2 - start2}s")
    extreme_puzzle = [
        [4,0,0,0,0,1,0,0,0,],
        [0,8,0,0,0,0,5,0,0,],
        [2,0,0,3,0,0,0,0,0,],
        [0,5,0,0,0,0,6,0,8,],
        [1,0,0,4,0,0,0,0,0,],
        [0,0,0,2,0,0,7,0,0,],
        [3,0,0,0,0,0,0,4,0,],
        [0,0,0,0,7,0,0,0,0,],
        [0,0,0,0,6,0,0,0,0,],
    ]
    EP = Puzzle(extreme_puzzle)
    print(EP.solve_optimized())