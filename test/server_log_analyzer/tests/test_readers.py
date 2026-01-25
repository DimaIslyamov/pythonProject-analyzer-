import unittest
from test.server_log_analyzer.readers.file_reader import FileReader


class TestFileReader(unittest.TestCase):

    def test_file_not_found(self):
        reader = FileReader("file_does_not_exist.txt")

        with self.assertRaises(FileNotFoundError):
            reader.read_lines()

            "https://github.com/DimaIslyamov/pythonProject-analyzer-.git"