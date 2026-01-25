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
    ]


@pytest.fixture
def list_reader(raw_lines):
    return ListReader(raw_lines)


@pytest.fixture
def simple_analyzer(list_reader):
    analyzer = SimpleLogAnalyzer(list_reader)
    analyzer.read()
    return analyzer


@pytest.fixture
def server_analyzer(list_reader):
    analyzer = ServerLogAnalyzer(list_reader)
    analyzer.read()
    return analyzer
