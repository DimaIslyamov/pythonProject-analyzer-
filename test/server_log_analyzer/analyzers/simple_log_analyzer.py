from test.server_log_analyzer.analyzers.base_log_analyzer import BaseLogAnalyzer


class SimpleLogAnalyzer(BaseLogAnalyzer):


    def analyze(self):
        for line in self.lines:
            if not line:
                continue

            self.stats['total'] += 1
