from test.server_log_analyzer.analyzers.base_log_analyzer import BaseLogAnalyzer


def run(analyzer: BaseLogAnalyzer):
    analyzer.read()
    analyzer.analyze()
    return analyzer.stats
