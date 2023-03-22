import os
from json_logger import file_logger


def test_file_logger(tmp_path):
    d = tmp_path / 'unit-test'
    d.mkdir()
    path = os.path.join(str(d), 'unit-test')
    file_logger(path=path, name='unit-test')
