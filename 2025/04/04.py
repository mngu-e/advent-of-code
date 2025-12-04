from utils import Solution, read_data
import time


class Day04Solution(Solution):
    def __init__(self):
        data = read_data("04")
        lines = data.split("\n")
        self.data = list(filter(None, lines))

    def get_cell(self, row, col):
        if 0 <= row < len(self.data) and 0 <= col < len(self.data[row]):
            return self.data[row][col]
        return 0

    def part1(self):
        acc = 0
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                adjacent_count = 0
                if self.data[row][col] == "@":
                    for dr, dc in directions:
                        if self.get_cell(row + dr, col + dc) == "@":
                            adjacent_count += 1
                    if adjacent_count < 4:
                        acc += 1
        print("part 1: ", acc)

    def remove_cell(self, grid):
        acc = 0
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                adjacent_count = 0
                if grid[row][col] == "@":
                    for dr, dc in directions:
                        if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[row]):
                            if grid[row + dr][col + dc] == "@":
                                adjacent_count += 1
                    if adjacent_count < 4:
                        str_as_list = list(grid[row])
                        str_as_list[col] = "."
                        grid[row] = "".join(str_as_list)
                        acc += 1
        return acc

    def part2(self):
        start_time = time.time()
        acc = 0
        grid = self.data.copy()
        while True:
            accX = self.remove_cell(grid)
            acc += accX
            if accX == 0:
                break
        print("--- %s seconds ---" % (time.time() - start_time))
        print("part 2: ", acc)


solution = Day04Solution()
