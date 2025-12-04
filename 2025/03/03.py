from utils import Solution, read_data


class Day03Solution(Solution):
    def __init__(self):
        data = read_data("03")
        lines = data.split("\n")
        self.data = list(filter(None, lines))

    def part1(self):
        acc = 0
        for line in self.data:
            x = 1
            l_max, r_max = int(line[0]), int(line[1])
            while x < len(line):
                if int(line[x]) > l_max and x != len(line) - 1:
                    l_max = int(line[x])
                    r_max = int(line[x + 1])
                elif int(line[x]) > r_max:
                    r_max = int(line[x])
                x += 1

            acc += int(str(l_max) + str(r_max))

        print("part 1:", acc)

    def part2(self):
        acc = 0
        for line in self.data:
            nums = []
            removed = 0
            to_remove = len(line) - 12
            for digit in line:
                while nums and int(nums[-1]) < int(digit) and removed < to_remove:
                    nums.pop()
                    removed += 1
                nums.append(digit)
            while removed < to_remove:
                nums.pop()
                removed += 1
            acc += int("".join(nums))
        print("part 2:", acc)


solution = Day03Solution()
