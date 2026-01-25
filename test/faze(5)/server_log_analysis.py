# step 1
def read_log(filename) -> list[str]:
    split_lines = []

    try:
        with open(filename, 'r') as f:
            content = f.readlines()

            for line in content:
                line = line.strip()
                split_lines.append(line)

                # 2 Небольшое улучшение
                # split_lines.append(line.strip())

    except FileNotFoundError:
        return []

    return split_lines


lines = read_log("../server_log_analyzer/server.log")
print(lines)


# step 2
def analyze_log(*, lines: list[str]) -> dict:
    stats = {
        "total": 0,
        "INFO": 0,
        "ERROR": 0,
        "WARNING": 0,
    }

    for line in lines:
        if not line:
            continue

        parts = line.split()
        if len(parts) < 2:
            continue

        level = parts[1]

        if level in stats:
            stats[level] += 1
            stats["total"] += 1

    return stats



analyzed_log = analyze_log(lines=lines)
print(analyzed_log)


# step 3
def write_report(stats: dict, filename: str):
    with open(filename, "w") as f:
        f.write(f"Total lines: {stats.get('total', 0)}\n")
        for level in ("INFO", "ERROR", "WARNING"):
            f.write(f"{level}: {stats.get(level, 0)}\n")



write_report(stats=analyzed_log, filename="../server_log_analyzer/analyzed_log.txt")


