import pytest
from test.server_log_analyzer.readers.file_reader import FileReader


def test_file_reader_raises_if_missing():
    reader = FileReader("server.log")

    with pytest.raises(FileNotFoundError):
        reader.read_lines()