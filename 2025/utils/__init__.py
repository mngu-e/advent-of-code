def read_data(day: str, is_practice: bool = False) -> list[str]:
    import sys
    if not is_practice:
        is_practice = "--practice" in sys.argv
    file = open(f"{day}/{"practice" if is_practice else "input"}.txt", "r")
    data = file.read()
    file.close()
    lines = data.split("\n")
    return list(filter(None, lines))

