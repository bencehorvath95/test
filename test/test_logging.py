from utils.logging import logger


def test_log_outside_request_context():
    """Logger should not raise when used outside a request context."""
    logger.info("outside context test")
