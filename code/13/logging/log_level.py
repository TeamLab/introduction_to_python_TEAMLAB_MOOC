import logging

logger = logging.getLogger("main")
stream_hander = logging.StreamHandler()
logger.addHandler(stream_hander)

logger.setLevel(logging.DEBUG)
logger.debug("틀렸잖아!")
logger.info("확인해")
logger.warning("조심해!")
logger.error("에러났어!!!")
logger.critical("망했다...")

logger.setLevel(logging.CRITICAL)
logger.debug("틀렸잖아!")
logger.info("확인해")
logger.warning("조심해!")
logger.error("에러났어!!!")
logger.critical("망했다...")
