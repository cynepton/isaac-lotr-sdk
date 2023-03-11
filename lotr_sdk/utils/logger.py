import logging

# Configure the logging module
def get_logger(name: str):
    """Logger object

    name (str): The module name

    Returns:
       `Logger`: The logger object
    """
    # Create a logger object
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create a console handler and set its log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter and add it to the console handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger to log to the console
    logger.addHandler(console_handler)

    return logger