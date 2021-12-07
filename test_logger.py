from Alogger import Alogger
logger = Alogger.Alogger(log_level=Alogger.LogLevel.ALL, log_to_file=False)

logger.fatal("fatal")
logger.error("error")
logger.warning("warning")
logger.info("info")
logger.debug("debug")
logger.trace("trace")
logger.test("test")
