from logs import bot_logger, server_logger, another_logger

server_logger.info("Example info message")
server_logger.warning("Example warning message")
server_logger.debug("Example debug message")

bot_logger.info("Example info message")
bot_logger.warning("Example warning message")
bot_logger.debug("Example debug message")

another_logger.info("Example info message")
another_logger.warning("Example warning message")
another_logger.debug("Example debug message")