import re
import pytest
from pathlib import Path


@pytest.fixture
def log_files() -> list[Path]:
    work_dir = Path.cwd().parent
    result = []
    for item in work_dir.iterdir():
        if item.name.startswith('log_'):
            result.append(item)
    return result


def test_errors_not_exists(log_files):
    pattern = r'(\[ERROR\])'
    errors = []
    for log in log_files:
        with open(log) as f:
            data = f.read()
            if match_data := re.findall(pattern=pattern, string=data):
                errors.extend(match_data)
    assert len(errors) == 0, 'Found errors in log files'

