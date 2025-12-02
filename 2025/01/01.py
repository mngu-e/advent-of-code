import math
from utils import Solution, read_data


class Day01Solution(Solution):
    def __init__(self):
        data = read_data("01")
        lines = data.split("\n")
        self.data = list(filter(None, lines))

    def part1(self):
        k = 0
        zeroes = 0
        for line in self.data:
            direction, number = line[0], int(line[1:])
            if direction == "L":
                k -= number
            else:
                k += number
            if (k / 50) % 2 == 1:
                zeroes += 1
        print("part 1:", zeroes)

    def part2(self):
        k = 50
        zeroes = 0
        for line in self.data:
            direction, number = line[0], int(line[1:])
            k_before = k
            k = k - number if direction == "L" else k + number
            if (k_before < 0 and k >= 0) or (k_before > 0 and k <= 0):
                zeroes += 1
            zeroes += int(math.floor(abs(k) / 100))
            k = abs(k % 100)
        print("part 2:", zeroes)


solution = Day01Solution()
