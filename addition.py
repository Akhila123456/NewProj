import logging

logger = logging.getLogger()
logging.basicConfig(filename='log_file',format='%(asctime)s %(message)s',filemode='w')
logger.setLevel(logging.INFO)
logger.info("Hello from Docker Python Image..!")