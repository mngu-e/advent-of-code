from utils import Solution, read_data


class Day05Solution(Solution):
    def __init__(self):
        data = read_data("05")
        ranges, ingredients = data.split("\n\n")
        ranges = ranges.split("\n")
        self.ranges = [
            list([int(line.split("-")[0]), int(line.split("-")[1])]) for line in ranges
        ]
        self.ingredients = list(filter(None, ingredients.split("\n")))
        print(self.ranges)
        print(self.ingredients)

    def part1(self):
        acc = 0
        for ingredient in self.ingredients:
            for range_start, range_end in self.ranges:
                if range_start <= int(ingredient) <= range_end:
                    acc += 1
                    break

        print("part 1: ", acc)

    def part2(self):
        ranges = []
        for range_start, range_end in sorted(self.ranges):
            if not ranges or ranges[-1][1] < range_start:
                ranges.append([range_start, range_end])
            else:
                ranges[-1][1] = max(ranges[-1][1], range_end)

        acc = 0
        for range_start, range_end in ranges:
            acc += range_end - range_start + 1

        print("part 2: ", acc)


solution = Day05Solution()
