import logging

logger = logging.getLogger("navi")

def emit_error() -> None:
    """
    Emit a error log message using the ``navi`` logger.

    This function is a simple example used to demonstrate Python's
    :mod:`logging` module and how to test log output with pytest's
    ``caplog`` fixture.
    """
    logger.error("⛔ ERROR ⛔")
    # logger.error("⛔ ERROR ⛔")
    # logger.error("⛔ ERROR ⛔")
    # logger.error("⛔ ERROR ⛔")
