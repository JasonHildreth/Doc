# Execute in Python3 
# Execution: python build_profiles.py
#			 python3 build_profiles.py


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
	import config as user
except ImportError:
	raise ImportError("\n\nProper config.py file not detected. See README.md\n")


PROFILE_PATH_PREFIX = "user-data-dir= "


profile_path_clean = PROFILE_PATH_PREFIX + user.PATH_TO_PROFILE_CLEAN
profile_path_block = PROFILE_PATH_PREFIX + user.PATH_TO_PROFILE_BLOCK

options_clean = webdriver.ChromeOptions()
options_block = webdriver.ChromeOptions()

options_clean.add_argument(profile_path_clean)
options_block.add_argument(profile_path_block)

print("Generating clean Chrome instance.")
driver_clean = webdriver.Chrome(chrome_options=options_clean)
print("Add Scalpel extension to Chrome in developer mode.")
print("Press enter when complete.")
input()
driver_clean.close()

print("Generating block Chrome instance.")
driver_block = webdriver.Chrome(chrome_options=options_block)
print("Add Scalpel extension to Chrome in developer mode.")
print("Add uMatrix to Chrome via Chrome Extension Store.")
print("Configure uMatrix to block first party and third party Javascript.")
print("Press enter when complete.")
input()
driver_block.close()