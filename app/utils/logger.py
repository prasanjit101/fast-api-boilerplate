import logging

# Set up logging to a file
logging.basicConfig(filename='app/logs/debug.txt', level=logging.DEBUG)
logging.basicConfig(filename='app/logs/info.txt', level=logging.INFO)