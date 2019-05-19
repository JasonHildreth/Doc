#	Doc Package
#	biopsy.py 
#	
#	Author: Jason Hildreth
#	Research Advisor: Dr. William C. Garrison III
#	University of Pittsburgh
#	Department of Computer Science
#
#	Primary tool for exporting data from website pages to files containing 
#	quantitative data. The config.py file must be correctly made, and the 
#	build_profiles.py script must have been run or else Biopsy will perform 
#	unpredictably. 


from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import manifest as manifest
import json
import time
import sys


try:
	import config as user
except ImportError:
	raise ImportError("\n\nProper config.py file not detected. See README.md\n")


BROWSER = "browser"
EXIT = "exit"
URL_PREFIX = "https://www."
FILE_TEXT_SUFFIX_CLEAN = "_clean.txt"
FILE_TEXT_SUFFIX_BLOCK = "_block.txt"
FILE_IMAGE_SUFFIX_CLEAN = "_clean.png"
FILE_IMAGE_SUFFIX_BLOCK = "_block.png"
PROFILE_PATH_PREFIX = "user-data-dir= "
WRITE_MODE = "w+"
DOM_DELIM_1 = "_BEGIN_DOM_"
DOM_DELIM_2 = "_END_DOM_"
DOM_TAG = "_DOM_"
HTTP_DELIM_1 = "BEGIN_HTTP_REQUEST_"
HTTP_DELIM_2 = "_END_HTTP_REQUEST_"
HTTP_TAG = "_HTTP_REQUEST_"
LOG_DELIM_1 = '{"level": "SEVERE", "message": '
LOG_DELIM_2 = '"source"'
LOG_TAG = "_LOG_"
DOM_FORMAT_REMOVE_1 = "\\\\\\\\\\\\\\"
DOM_FORMAT_OPENING_BRACE = "{"
DOM_FORMAT_CLOSING_BRACE = "}"


def strip_JSON(entry):
    """ Strips JSON notation and returns the item as the original string. """
    stripped_entry = ""
    if (HTTP_DELIM_1 in entry): 
        stripped_entry = strip_http_request_entry(entry)
        stripped_entry = HTTP_TAG + stripped_entry

    elif (DOM_DELIM_1 in entry):
        stripped_entry = strip_DOM(entry)

        stripped_entry = DOM_TAG + stripped_entry

    else:
        stripped_entry = strip_log_entry(entry)
        stripped_entry = LOG_TAG + stripped_entry

    return stripped_entry


def strip_http_request_entry(entry):
    """ Strips console log JSON format off of a http request entry. Returns the
        entry without an identifying tag. """
    stripped_entry = ""
    split_first_section = entry.split(HTTP_DELIM_1)
    split_second_section = split_first_section[1].split(HTTP_DELIM_2)
    stripped_entry = split_second_section[0]

    return stripped_entry


def strip_log_entry(entry):
    """ Removes console log JSON format off of a log entry. Returns the entry 
        without an identifying tag. """
    stripped_entry = ""
    split_entry = entry.split(LOG_DELIM_1)
    for i in range(0, len(split_entry)):
        if LOG_DELIM_2 in split_entry[i]:
            split_entry_again = split_entry[i].split(LOG_DELIM_2)
            stripped_entry = split_entry_again[0]

    return stripped_entry


def strip_DOM(dom):
    """ Removes the console.log JSON format from a DOM entry. Returns the entry
        without an identifying tag. """
    stripped_dom = ""

    dom_string = json.dumps(dom)

    first_split = dom_string.split(DOM_DELIM_1)
    second_split = first_split[1].split(DOM_DELIM_2)
    stripped_dom = second_split[0]

    formatted_dom = stripped_dom.replace(DOM_FORMAT_REMOVE_1, "")

    return formatted_dom


def process_website(driver_clean, driver_block, website_id, ask_for_confirmation):
	""" Processes a website and exports the files """
	website_url = URL_PREFIX + website_id
	directory_path = user.PATH_TO_STORE_DATA

	filename_clean = website_id + FILE_TEXT_SUFFIX_CLEAN
	filename_block = website_id + FILE_TEXT_SUFFIX_BLOCK

	path_to_write_clean = directory_path + filename_clean
	path_to_write_block = directory_path + filename_block

	output_clean = open(path_to_write_clean, WRITE_MODE)
	output_block = open(path_to_write_block, WRITE_MODE)

	driver_clean.get(website_url)
	driver_block.get(website_url)

	time.sleep(user.SECONDS_TO_WAIT)

	output_clean.write(website_url + "\n")
	output_block.write(website_url + "\n")

	for entry in driver_clean.get_log(BROWSER):
		output_clean.write(strip_JSON(json.dumps(entry)))
		output_clean.write("\n")

	for entry in driver_block.get_log(BROWSER):
		output_block.write(strip_JSON(json.dumps(entry)))
		output_block.write("\n")

	driver_clean.save_screenshot(directory_path + website_id + FILE_IMAGE_SUFFIX_CLEAN)
	driver_block.save_screenshot(directory_path + website_id + FILE_IMAGE_SUFFIX_BLOCK)

	if (ask_for_confirmation == True):
		input("Press enter to proceed to the next item in manifest.")

	output_clean.close()
	output_block.close()


def main():
	profile_path_clean = PROFILE_PATH_PREFIX + user.PATH_TO_PROFILE_CLEAN
	profile_path_block = PROFILE_PATH_PREFIX + user.PATH_TO_PROFILE_BLOCK
	options_clean = webdriver.ChromeOptions()
	options_block = webdriver.ChromeOptions()
	options_clean.add_argument(profile_path_clean)
	options_block.add_argument(profile_path_block)

	driver_clean = webdriver.Chrome(chrome_options=options_clean)
	driver_block = webdriver.Chrome(chrome_options=options_block)
	argument_total = len(sys.argv)

	if (argument_total == 2 and str(sys.argv[1]) == "-m"):
		# process manifest file
		for entry in manifest.MANIFEST:
			website_id = entry[0];
			print("Processing " + website_id)
			process_website(driver_clean, driver_block, website_id, True)
	else:
		# ask for website and process one at a time 
		while(True):
			website_id = input("Website URL (only domain and TLD): (\"exit\" to exit): ")
			if (website_id == EXIT):
				driver_clean.close()
				driver_block.close()
				exit()

			process_website(driver_clean, driver_block, website_id, False)


if __name__ == "__main__":
	main()
