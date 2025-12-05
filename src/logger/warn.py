import logging

logger = logging.getLogger("navi")

def emit_warning() -> None:
    """
    Emit a warning log message using the ``navi`` logger.

    This function is a simple example used to demonstrate Python's
    :mod:`logging` module and how to test log output with pytest's
    ``caplog`` fixture.
    """
    logger.warning("⚠️⚠️⚠️ OH-OH Warning ⚠️⚠️⚠️")
    # logger.warning("⚠️⚠️⚠️ OH-OH Warning ⚠️⚠️⚠️")
    # logger.warning("⚠️⚠️⚠️ OH-OH Warning ⚠️⚠️⚠️")
    # logger.warning("⚠️⚠️⚠️ OH-OH Warning ⚠️⚠️⚠️")
