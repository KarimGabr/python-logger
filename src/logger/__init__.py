import logging
from .warn import emit_warning

logging.basicConfig()  # configures logger with default settings

logger = logging.getLogger("navi")  # get or create a logger named "navi"
logger.setLevel(logging.INFO)  # set level to INFO, anything below is not emitted

# logger.warning("WARNING111!")
# logger.critical("1111 THIS IS SO CRITICAL XDXDXDXDXDXDXD !!!!")
logger.debug("Wake-up call ...")
logger.info("Hey! Listen!")
# logger.info("Hey! Listen!")
# logger.debug("Wake-up call ...")
# logger.debug("Wake-up call ...")
# logger.info("Hey! Listen!")
# logger.critical("222 THIS IS SO CRITICAL XDXDXDXDXDXDXD !!!!")
# logger.info("Hey! Listen!")
# logger.warning("WARNING!")
# logger.error("ERRORRRRR!")

__all__ = ["emit_warning"]
