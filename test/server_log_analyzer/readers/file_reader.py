from test.server_log_analyzer.readers.reader import Reader

class FileReader:
    def __init__(self, filename):
        self._filename = filename


    def read_lines(self) -> list[str]:
        lines = []
        with open(self._filename, 'r') as f:
            for line in f:
                lines.append(line.strip())

        return lines