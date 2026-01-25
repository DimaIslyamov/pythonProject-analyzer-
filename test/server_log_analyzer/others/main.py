from test.server_log_analyzer.readers.file_reader import FileReader
from test.server_log_analyzer.analyzers.server_log_analyzer import ServerLogAnalyzer
from run import run


def main():
    reader = FileReader("server.log")
    analyzer = ServerLogAnalyzer(reader)

    stats = run(analyzer)

    print(stats)


if __name__ == "__main__":
    main()
