# Template file for creating a configuration to enable persistence
# File must be saved as "config.py" in order to work properly

# Time to force the Python interpreter to sleep to allow Selenium to fully
# load before beginning work 
# Not recommended to go below 5
TIME_TO_WAIT = 5

# Obtain path by navigating Chrome to "Chrome://Version"
# Path must be absolute
PATH_TO_PROFILE_CLEAN = "PATH HERE"
PATH_TO_PROFILE_BLOCK = "PATH HERE"

# Data files collected will be written and stored here
# Path doesn't need to be absolute but can be
PATH_TO_STORE_DATA = "PATH HERE"