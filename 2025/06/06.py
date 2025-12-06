from utils import Solution, read_data


class Day06Solution(Solution):
    def __init__(self):
        self.data = [list(line) for line in filter(None, read_data("06").split("\n"))]

    def part1(self):
        acc = 0
        curr_start, curr_end = None, None
        curr_operation = None
        for index, symbol in enumerate(self.data[-1]):
            if symbol in ["*", "+"] or index == len(self.data[-1]) - 1:
                if curr_start is None:
                    curr_start = index
                    curr_operation = symbol
                else:
                    curr_end = index - 1 if index != len(self.data[-1]) - 1 else index

                    curr_acc = int("".join(self.data[0][curr_start : curr_end + 1]))
                    for row in self.data[1 : len(self.data) - 1]:
                        num = int("".join(row[curr_start : curr_end + 1]))
                        if curr_operation == "*":
                            curr_acc *= num
                        else:
                            curr_acc += num
                    acc += curr_acc
                    curr_operation = symbol
                    curr_start, curr_end = index, None
        # 6605396225322
        print("part 1:", acc)

    def part2(self):
        acc = 0
        curr_start, curr_end = None, None
        curr_operation = None
        for index, symbol in enumerate(self.data[-1]):
            if symbol in ["*", "+"] or index == len(self.data[-1]) - 1:
                if curr_start is None:
                    curr_start = index
                    curr_operation = symbol
                else:
                    curr_end = index - 1 if index != len(self.data[-1]) - 1 else index
                    curr_acc = 1 if curr_operation == "*" else 0
                    for i in range(curr_end, curr_start - 1, -1):
                        num = []
                        for row in self.data[0 : len(self.data) - 1]:
                            if row[i] != " ":
                                num.append(row[i])
                        if len(num) == 0:
                            continue
                        if curr_operation == "*":
                            curr_acc *= int("".join(num).strip())
                        else:
                            curr_acc += int("".join(num).strip())
                    acc += curr_acc
                    curr_operation = symbol
                    curr_start, curr_end = index, None
        # 11052310600986
        print("part 2:", acc)


solution = Day06Solution()
