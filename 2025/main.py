import sys
import importlib


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <day ('01')> <part1 or part2> [--practice]")
        sys.exit(1)

    day = sys.argv[1].zfill(2)

    try:
        day_module = importlib.import_module(f"{day}.{day}")
        is_part_1 = sys.argv[2] == "part1"
        day_module.solution.part1() if is_part_1 else day_module.solution.part2()

    except ImportError:
        print(f"Day {day} module not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
