import pytest
from test.server_log_analyzer.readers.list_reader import ListReader
from test.server_log_analyzer.analyzers.simple_log_analyzer import SimpleLogAnalyzer


@pytest.mark.parametrize(
    "lines, expected_total",
    [
        (["one", "two"], 2),
        (["one", "", "two"], 2),
        (["", "", ""], 0),
        ([], 0),
        (["a", "b", "c"], 3),
    ]
)


def test_simple_log_analyzer_counts_non_empty_lines(lines, expected_total):
    reader = ListReader(lines)
    analyzer = SimpleLogAnalyzer(reader)

    analyzer.read()
    analyzer.analyze()

    assert analyzer.stats["total"] == expected_total



    # структура для  @pytest.mark.parametrize
    # @pytest.mark.parametrize(
    #     "input_data, expected",
    #     [
    #         (данные_1, результат_1),
    #         (данные_2, результат_2),
    #     ]
    # )
    # def test_something(input_data, expected):
    #     ...
