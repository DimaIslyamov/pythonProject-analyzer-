import pytest
from test.server_log_analyzer.readers.list_reader import ListReader
from test.server_log_analyzer.analyzers.simple_log_analyzer import SimpleLogAnalyzer
from test.server_log_analyzer.analyzers.server_log_analyzer import ServerLogAnalyzer


@pytest.fixture
def raw_lines():
    return [
        "2024-01-01 INFO Test",
        "2024-01-02 ERROR Fail",
        "",
        "invalid line",
        "2024-01-01 INFO User logged in",
        "2024-01-01 ERROR Invalid password",
        "2024-01-02 WARNING Low memory"
        "123 23124 6t31 12",

    ]


@pytest.fixture
def list_reader(raw_lines):
    return ListReader(raw_lines)


@pytest.fixture
def simple_analyzer_factory():

    def _factory(lines: list[str]):
        reader = ListReader(lines)
        analyzer = SimpleLogAnalyzer(reader)
        analyzer.read()
        return analyzer

    return _factory


@pytest.fixture
def server_analyzer_factory():

    def _factory(lines: list[str]):
        reader = ListReader(lines)
        analyzer = ServerLogAnalyzer(reader)
        analyzer.read()
        return analyzer

    return _factory
