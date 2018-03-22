### copy this ##
def setup_logger(self, logger_name, log_file, level=logging.INFO):
	"""
	Args:
		logger_name: The name that will be assigned to configured logger.
		log_file: the location which this log want to be saved.
		level: what is the raise level of this log.

	Returns:
	"""
	new_logger = logging.getLogger(logger_name)
	formatter = logging.Formatter('%(asctime)s : %(message)s')
	fileHandler = logging.FileHandler(log_file)
	fileHandler.setFormatter(formatter)
	streamHandler = logging.StreamHandler()
	streamHandler.setFormatter(formatter)

	new_logger.setLevel(level)
	new_logger.addHandler(fileHandler) # where the log will be stored.
	new_logger.addHandler(streamHandler)  # how this will looks like.
	
	
### use it as:
self.setup_logger('creation_logger', "C:/ConsumerTMS/logs/resource_monitor.log")
self.check_creation_logger = logging.getLogger('creation_logger')