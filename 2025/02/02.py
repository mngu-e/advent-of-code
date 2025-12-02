from utils import Solution, read_data


class Day02Solution(Solution):
    def __init__(self):
        data = read_data("02")
        lines = data.split(",")
        self.data = list(filter(None, lines))

    def part1(self):
        acc = 0
        for range_string in self.data:
            start, end = range_string.split("-")
            for i in range(int(start), int(end) + 1):
                s = str(i)
                if len(s) % 2 == 0:
                    mid = len(s) // 2
                    if s[:mid] == s[mid:]:
                        acc += i

        print("part 1:", acc)

    def part2(self):
        acc = 0
        for range_string in self.data:
            start, end = range_string.split("-")
            for i in range(int(start), int(end) + 1):
                s = str(i)
                is_invalid = False
                for pattern_length in range(1, len(s) // 2 + 1):
                    if len(s) % pattern_length == 0:
                        pattern = s[:pattern_length]
                        if pattern * (len(s) // pattern_length) == s:
                            is_invalid = True
                            break
                if is_invalid:
                    acc += i
        print("part 2:", acc)


solution = Day02Solution()
