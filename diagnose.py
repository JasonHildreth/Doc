#	Doc Package
#	diagnose.py
#	
#	Author: Jason Hildreth
#	Research Advisor: Dr. William C. Garrison III
#	University of Pittsburgh
#	Department of Computer Science
#
#	Execution:
#		python3 diagnose.py <WEBSITE_URL>
#
#	Takes in a website URL, performs two-pass analysis, and exports the fault, 
#	if present. 

import sys
from website import Website 
from website import WebsitePair


def page_is_blank(clean, block, pair):
	"""Determines if a website page is blank. 
		Return:
			True if page is blank.
			False otherwise.	
	"""
	white_pixel_ratio = block.get_white_to_total_ratio()

	if white_pixel_ratio == 1:
		return True

	elif white_pixel_ratio >= 0.75:
		white_pixel_change = pair.get_white_pixel_change_proportion()

		if white_pixel_change >= 0.5:
			return True

		else:
			return False

	else:
		return False


def main():
	if len(sys.argv) != 2:
		print("Invalid command line arguments.")
		print("Usage: python3 diagnose.py <WEBSITE_URL>")
		exit()

	url = sys.argv[1]

	FILEPATH_PREFIX = "data/"
	FILEPATH_TEXT_SUFFIX_CLEAN = "_clean.txt"
	FILEPATH_TEXT_SUFFIX_BLOCK = "_block.txt"
	FILEPATH_IMAGE_SUFFIX_CLEAN = "_clean.png"
	FILEPATH_IMAGE_SUFFIX_BLOCK = "_block.png"

	txt_clean = FILEPATH_PREFIX + url + FILEPATH_TEXT_SUFFIX_CLEAN
	txt_block = FILEPATH_PREFIX + url + FILEPATH_IMAGE_SUFFIX_BLOCK
	img_clean = FILEPATH_PREFIX + url + FILEPATH_IMAGE_SUFFIX_CLEAN
	img_block = FILEPATH_PREFIX + url + FILEPATH_IMAGE_SUFFIX_BLOCK

	website_clean = Website(txt_clean, img_clean, "clean")
	website_block = Website(txt_block, img_block, "block")
	pair = WebsitePair(website_clean, website_block)

	# @TODO This if-else section can be expanded as future faults become detectable. 
	if page_is_blank(website_clean, website_block, pair):
		print("Page is blank!")

	else:
		print("No faults detected.")




if __name__ == "__main__":
	main()