from utils import Solution, read_data
import time


class Day04Solution(Solution):
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

    def __init__(self):
        self.data = read_data("04")

    def get_cell(self, grid, row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
            return grid[row][col]
        return 0

    def part1(self):
        acc = 0
        lines = self.data.split("\n")
        grid = list(filter(None, lines))
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                adjacent_count = 0
                if grid[row][col] == "@":
                    for dr, dc in self.directions:
                        if self.get_cell(grid, row + dr, col + dc) == "@":
                            adjacent_count += 1
                    if adjacent_count < 4:
                        acc += 1
        print("part 1: ", acc)

    def part2(self):
        self.part2dfs()
        self.part2brute()

    def part2brute(self):
        lines = self.data.split("\n")
        grid = [list(line) for line in filter(None, lines)]
        start_time = time.time()
        acc = 0
        while True:
            curr_acc = 0
            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    adjacent_count = 0
                    if grid[row][col] == "@":
                        for dr, dc in self.directions:
                            if self.get_cell(grid, row + dr, col + dc) == "@":
                                adjacent_count += 1
                        if adjacent_count < 4:
                            grid[row][col] = "."
                            curr_acc += 1
            if curr_acc == 0:
                break
            acc += curr_acc

        print("--- %s seconds ---" % (time.time() - start_time))
        print("part 2 brute: ", acc)

    def part2dfs(self):
        from collections import deque

        lines = self.data.split("\n")
        grid = [list(line) for line in filter(None, lines)]
        start_time = time.time()

        queue = deque()
        queued = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                adjacent_count = 0
                if grid[row][col] == "@":
                    for dr, dc in self.directions:
                        if self.get_cell(grid, row + dr, col + dc) == "@":
                            adjacent_count += 1
                    if adjacent_count < 4:
                        queue.append((row, col))
                        queued.add((row, col))
        acc = 0
        while queue:
            row, col = queue.popleft()
            queued.remove((row, col))

            if grid[row][col] != "@":
                continue

            grid[row][col] = "."
            acc += 1

            for dr, dc in self.directions:
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < len(grid)
                    and 0 <= nc < len(grid[nr])
                    and grid[nr][nc] == "@"
                    and (nr, nc) not in queued
                ):
                    adjacent_count = 0
                    for ndr, ndc in self.directions:
                        if self.get_cell(grid, nr + ndr, nc + ndc) == "@":
                            adjacent_count += 1
                    if adjacent_count < 4:
                        queue.append((nr, nc))
                        queued.add((nr, nc))
        print("--- %s seconds ---" % (time.time() - start_time))
        print("part 2 dfs: ", acc)


solution = Day04Solution()
