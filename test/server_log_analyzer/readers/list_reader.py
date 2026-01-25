from test.server_log_analyzer.readers.reader import Reader

class ListReader:
    def __init__(self, lines: list[str]):
        self._lines = lines

    def read_lines(self) -> list[str]:
        return [line.strip() for line in self._lines]
