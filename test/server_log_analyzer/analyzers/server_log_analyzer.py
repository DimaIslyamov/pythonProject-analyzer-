from test.server_log_analyzer.readers.list_reader import ListReader
from test.server_log_analyzer.analyzers.base_log_analyzer import BaseLogAnalyzer
from test.server_log_analyzer.readers.file_reader import Reader
from test.server_log_analyzer.analyzers.simple_log_analyzer import SimpleLogAnalyzer
from test.server_log_analyzer.core.run import run

LOG_LEVELS = ("INFO", "ERROR", "WARNING")


class ServerLogAnalyzer(BaseLogAnalyzer):
    def __init__(self, read: Reader):
        super().__init__(read)


        for level in LOG_LEVELS:
            self.stats[level] = 0


    def analyze(self):
        for line in self.lines:
            if not line:
                continue

            parts = line.split()
            if len(parts) < 2:
                continue

            level = parts[1]
            if level in self.stats:
                self.stats[level] += 1
                self.stats["total"] += 1


    def write_report(self, output_filename: str):
        with open(output_filename, "w") as f:
            f.write(f"Total lines: {self.stats.get('total', 0)}\n")
            for level in LOG_LEVELS:
                f.write(f"{level}: {self.stats.get(level, 0)}\n")





test_lines = [
    "2024-01-01 INFO Test message",
    "2024-01-02 ERROR Something broke",
    "",
    "invalid line",
    "2024-01-01 INFO User logged in",
    "2024-01-01 ERROR Invalid password",
    "2024-01-02 INFO Page opened",
    "2024-01-02 WARNING Low memory",
    "Star wars 123 clone attack",
    "2024-01-03 ERROR Connection lost",
    "44 22 345 654",
]

#reader = FileReader("server.log")
reader = ListReader(test_lines)

simple_analyzer = SimpleLogAnalyzer(reader)
server_analyzer = ServerLogAnalyzer(reader)

print(run(simple_analyzer))
print(run(server_analyzer))


