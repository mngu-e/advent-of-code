def read_data(day: str, is_practice: bool = False) -> list[str]:
    file = open(f"{day}/{"practice" if is_practice else "input"}.txt", "r")
    data = file.read()
    file.close()
    lines = data.split("\n")
    return list(filter(None, lines))

