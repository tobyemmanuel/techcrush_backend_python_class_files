# Introduction to Logging

# Used to record messages about a program’s execution.
# Helps in debugging and monitoring.


# The logging Module
# Provides a flexible way to log messages.


import logging

logging.basicConfig(
    filename="app.log",              # Log file name
    level=logging.DEBUG,             # Log all levels DEBUG and above
    format="%(asctime)s - %(levelname)s - %(message)s" # Format for logging
)

# logging.info("This is an info message.")
# logging.error("This is an error message.")


# Logging Levels
# Level -       Purpose
# DEBUG	-       Detailed information for debugging.
# INFO -        General information about execution.
# WARNING -     An indication of potential problems.
# ERROR -       A serious issue occurred.
# CRITICAL -    A severe error causing program crash.


# Writing Logs to a File
# logging.basicConfig(filename="./app.log", level=logging.INFO)
# logging.info("Program started")
# logging.warning("This is a warning")
# logging.error("An error occurred")


def greet():
    logging.critical("Program started")
    
    for i in range(10):
        print(i)
    logging.critical("Program finished")

greet()

# Different Loggers and Handlers
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(lineno)d - %(message)s")


critical_logging = logging.FileHandler("critical.log")
critical_logging.setLevel(logging.CRITICAL)
critical_logging.setFormatter(formatter)

debug_logging = logging.FileHandler("debug.log")
debug_logging.setLevel(logging.DEBUG)
debug_logging.setFormatter(formatter)

logger.addHandler(critical_logging)
logger.addHandler(debug_logging)

logger.debug("This is a debug message")
logger.critical("This is a critical message")

# INSTRUCTIONS FOR TESTING
# 1. Launch your terminal and run the code
# 2. Run the code -> python 16_python_logging.py