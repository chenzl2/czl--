import time
from utils.configure import Environment
from utils.send_message import SendMessage


def pytest_terminal_summary(terminalreporter, config):
    if not hasattr(config, 'workeroutput'):
        passed = len([i for i in terminalreporter.stats.get("passed", []) if i.when != 'teardown'])
        failed = len([i for i in terminalreporter.stats.get("failed", []) if i.when != 'teardown'])
        error = len([i for i in terminalreporter.stats.get("error", []) if i.when != 'teardown'])
        skipped = len([i for i in terminalreporter.stats.get("skipped", []) if i.when != 'teardown'])
        duration = time.time() - terminalreporter._sessionstarttime
        total = passed + failed + error
        content = Environment.report_template.format(total, passed, failed, error, skipped,
                                         round(passed / total * 100), round(duration))
        SendMessage(content).send()

