def read_data(day: str, is_practice: bool = False) -> str:
    import sys

    if not is_practice:
        is_practice = "--practice" in sys.argv
    file = open(f"{day}/{"practice" if is_practice else "input"}.txt", "r")
    data = file.read()
    file.close()
    return data


class Solution:

    def part1(self):
        pass

    def part2(self):
        pass
