from pathlib import Path
import inspect
import logging
import pytest

@pytest.mark.usefixtures("setup02")
class TestBaseClass(object):
    
    BASE_FILE=Path(__file__).resolve().parent.parent
    LOG_FILE=BASE_FILE.joinpath("Logs").joinpath("test_lambda.log")
    
    def get_logger(self)->logging.getLogger:
        logger = logging.getLogger(name=inspect.stack()[1][3])
        logger.setLevel(logging.INFO)
        filehandler=logging.FileHandler(self.LOG_FILE)
        filehandler.setLevel(logging.INFO)
        formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        return logger