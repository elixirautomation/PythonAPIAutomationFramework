import pytest


@pytest.fixture(scope="session")
def rp_logger(request):
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    if hasattr(request.node.config, 'py_test_service'):
        from pytest_reportportal import RPLogger, RPLogHandler
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
    else:
        import sys
        rp_handler = logging.StreamHandler(sys.stdout)
    rp_handler.setLevel(logging.INFO)
    return logger
