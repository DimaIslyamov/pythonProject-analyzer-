#import unittest
from test.server_log_analyzer.readers.list_reader import ListReader
from test.server_log_analyzer.analyzers.server_log_analyzer import ServerLogAnalyzer
from test.server_log_analyzer.analyzers.simple_log_analyzer import SimpleLogAnalyzer


def test_simple_log_analyzer_counts_non_empty_lines(simple_analyzer):
    simple_analyzer.analyze()
    assert simple_analyzer.stats["total"] == 6

    # lines = ["one", "two", "", "three"]
#
#     reader = ListReader(lines)
#     analyzer = SimpleLogAnalyzer(reader)
#
#     analyzer.read()
#     analyzer.analyze()
#
#     assert analyzer.stats["total"] == 3


def test_server_log_analyzer_counts_levels(server_analyzer):
    server_analyzer.analyze()

    assert server_analyzer.stats["INFO"] == 2
    assert server_analyzer.stats["ERROR"] == 2
    assert server_analyzer.stats["WARNING"] == 1
    assert server_analyzer.stats["total"] == 5



    # lines = [
#         "2024-01-01 INFO Test",
#         "2024-01-02 ERROR Fail",
#         "",
#         "invalid"
#     ]
#
#     reader = ListReader(lines)
#     analyzer = ServerLogAnalyzer(reader)
#
#     analyzer.read()
#     analyzer.analyze()
#
#     assert analyzer.stats["INFO"] == 1
#     assert analyzer.stats["ERROR"] == 1
#     assert analyzer.stats["WARNING"] == 0
#     assert analyzer.stats["total"] == 2



# Тесты через unittest
# class TestSimpleLogAnalyzer(unittest.TestCase):
#     def test_simple_log_analyzer_counts_non_empty_lines(self):
#         lines = [
#             "line ome",
#             "",
#             "line two",
#         ]
#
#         reader = ListReader(lines)
#         analyzer = SimpleLogAnalyzer(reader)
#
#         analyzer.read()
#         analyzer.analyze()
#
#         self.assertEqual(analyzer.stats["total"], 2)
#
#
#
# class TestServerLogAnalyzer(unittest.TestCase):
#     def test_server_log_analyzer_ignores_invalid_lines(self):
#         lines = [
#             "INFO",  # одно слово
#             "2024-01-01",  # дата без уровня
#             "2024-01-01 DEBUG Test",  # неизвестный уровень
#             "",  # пустая
#             "Just some random text"
#         ]
#
#         reader = ListReader(lines)
#         analyzer = ServerLogAnalyzer(reader)
#
#         analyzer.read()
#         analyzer.analyze()
#
#         self.assertEqual(analyzer.stats["INFO"], 0)
#         self.assertEqual(analyzer.stats["ERROR"], 0)
#         self.assertEqual(analyzer.stats["WARNING"], 0)
#         self.assertEqual(analyzer.stats["total"], 0)
#
#
#     def test_server_log_analyzer_counts_log_levels(self):
#         lines = [
#             "2024-01-01 INFO Test",
#             "2024-01-02 ERROR Fail",
#             "",
#             "invalid line"
#         ]
#
#         reader = ListReader(lines)
#         analyzer = ServerLogAnalyzer(reader)
#
#         analyzer.read()
#         analyzer.analyze()
#
#         self.assertEqual(analyzer.stats["INFO"], 1)
#         self.assertEqual(analyzer.stats["ERROR"], 1)
#         self.assertEqual(analyzer.stats["WARNING"], 0)
#         self.assertEqual(analyzer.stats["total"], 2)


#if __name__ == "__main__":
#    unittest.main()




# Правка с использованием @pytest.fixture
# import pytest
# from readers.list_reader import ListReader
# from analyzers.simple_log_analyzer import SimpleLogAnalyzer
# from analyzers.server_log_analyzer import ServerLogAnalyzer
#
#
# @pytest.fixture
# def list_reader():
#     lines = [
#         "2024-01-01 INFO Test",
#         "",
#         "2024-01-02 ERROR Fail"
#     ]
#     return ListReader(lines)
#
#
# @pytest.fixture
# def simple_analyzer(list_reader):
#     analyzer = SimpleLogAnalyzer(list_reader)
#     analyzer.read()
#     return analyzer
#
#
# @pytest.fixture
# def server_analyzer(list_reader):
#     analyzer = ServerLogAnalyzer(list_reader)
#     analyzer.read()
#     return analyzer
#
#
# def test_simple_log_analyzer_counts_non_empty_lines(simple_analyzer):
#     simple_analyzer.analyze()
#     assert simple_analyzer.stats["total"] == 2
#
#
# def test_server_log_analyzer_counts_levels(server_analyzer):
#     server_analyzer.analyze()
#
#     assert server_analyzer.stats["INFO"] == 1
#     assert server_analyzer.stats["ERROR"] == 1
#     assert server_analyzer.stats["WARNING"] == 0