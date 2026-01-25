from abc import ABC, abstractmethod
from test.server_log_analyzer.readers.file_reader import Reader


class BaseLogAnalyzer(ABC):
    def __init__(self, reader: Reader):
        self.reader = reader
        self.lines: list[str] = []
        self.stats: dict[str, int] = {"total": 0}


    def read(self):
        self.lines = self.reader.read_lines()


    @abstractmethod
    def  analyze(self):
        pass