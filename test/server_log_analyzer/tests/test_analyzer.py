import unittest
from test.server_log_analyzer.readers.list_reader import ListReader
from test.server_log_analyzer.analyzers.server_log_analyzer import ServerLogAnalyzer
from test.server_log_analyzer.analyzers.simple_log_analyzer import SimpleLogAnalyzer


class TestSimpleLogAnalyzer(unittest.TestCase):


    def test_simple_log_analyzer_counts_non_empty_lines(self):
        lines = [
            "line ome",
            "",
            "line two",
        ]

        reader = ListReader(lines)
        analyzer = SimpleLogAnalyzer(reader)

        analyzer.read()
        analyzer.analyze()

        self.assertEqual(analyzer.stats["total"], 2)



class TestServerLogAnalyzer(unittest.TestCase):


    def test_server_log_analyzer_counts_log_levels(self):
        lines = [
            "2024-01-01 INFO Test",
            "2024-01-02 ERROR Fail",
            "",
            "invalid line"
        ]

        reader = ListReader(lines)
        analyzer = ServerLogAnalyzer(reader)

        analyzer.read()
        analyzer.analyze()

        self.assertEqual(analyzer.stats["INFO"], 1)
        self.assertEqual(analyzer.stats["ERROR"], 1)
        self.assertEqual(analyzer.stats["WARNING"], 0)
        self.assertEqual(analyzer.stats["total"], 2)



if __name__ == "__main__":
    unittest.main()

