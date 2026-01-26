import pytest
from test.server_log_analyzer.readers.list_reader import ListReader
from test.server_log_analyzer.analyzers.server_log_analyzer import ServerLogAnalyzer


@pytest.mark.parametrize(
    "lines, expected",
    [
        (
            [
                "2024-01-01 INFO Test",
                "2024-01-02 ERROR Fail",
            ],
            {"INFO": 1, "ERROR": 1, "WARNING": 0, "total": 2},
        ),
        (
            [
                "2024-01-01 INFO Test",
                "",
                "invalid line",
            ],
            {"INFO": 1, "ERROR": 0, "WARNING": 0, "total": 1},
        ),
        (
            [],
            {"INFO": 0, "ERROR": 0, "WARNING": 0, "total": 0},
        ),
    ]
)


def test_server_log_analyzer_parametrized(lines, expected):
    reader = ListReader(lines)
    analyzer = ServerLogAnalyzer(reader)

    analyzer.read()
    analyzer.analyze()

    for key, value in expected.items():
        assert analyzer.stats[key] == value
