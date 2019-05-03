#	Doc Package
#	export_to_csv.py
#
#	Executions:
#		python3 export_to_csv.py 
#			Writes a CSV line of data for every website in the manifest. Can be redirected
#			to a file. 
#		python3 export_to_csv.py <URL> 
#			Writes a CSV line of data for <URL>. Can be redirected to a file.
#
#	Dependencies:
#		- website.py
#	
#	Author: Jason Hildreth
#	Research Advisor: Dr. William C. Garrison III
#	University of Pittsburgh
#	Department of Computer Science
#	
#	The export_to_csv tool exports parameters of Website and WebsitePair objects in 
#	comma-separated-values format for analysis. 

import sys
import manifest as manifest
from website import Website
from website import WebsitePair


FILEPATH_PREFIX = "data/"
FILEPATH_TEXT_SUFFIX_CLEAN = "_clean.txt"
FILEPATH_TEXT_SUFFIX_BLOCK = "_block.txt"
FILEPATH_IMAGE_SUFFIX_CLEAN = "_clean.png"
FILEPATH_IMAGE_SUFFIX_BLOCK = "_block.png"


def get_csv_header(clean, block, pair):
	"""Builds the master csv header from both Website objects and the WebsitePair 
	object.
	"""
	csv = ""
	csv = csv + clean.get_csv_header(True)
	csv = csv + block.get_csv_header(False)
	csv = csv + pair.get_csv_header()


def get_csv_string(clean, block, pair):
	"""Builds the csv string for a website from both Website objects and the WebsitePair
	object.
	"""
	csv = ""
	csv = csv + clean.to_csv(True)
	csv = csv + block.to_csv(False)
	csv = csv + pair.to_csv()
	return csv


def process_single_website(website_url):
	"""Processes a single website and exports to csv string.
	"""
	txt_clean = FILEPATH_PREFIX + website_url + FILEPATH_TEXT_SUFFIX_CLEAN
	txt_block = FILEPATH_PREFIX + website_url + FILEPATH_IMAGE_SUFFIX_BLOCK
	img_clean = FILEPATH_PREFIX + website_url + FILEPATH_IMAGE_SUFFIX_CLEAN
	img_block = FILEPATH_PREFIX + website_url + FILEPATH_IMAGE_SUFFIX_BLOCK

	website_clean = Website(txt_clean, img_clean, "clean")
	website_block = Website(txt_block, img_block, "block")
	pair = WebsitePair(website_clean, website_block)

	print(get_csv_header(website_clean, website_block, pair))


def process_manifest():
	"""Processes all websites in the manifest.
	"""
	m = manifest.MANIFEST
	for i in range(0, len(m)):
		entry = m[i]

		txt_clean = FILEPATH_PREFIX + entry[0] + FILEPATH_TEXT_SUFFIX_CLEAN
		txt_block = FILEPATH_PREFIX + entry[0] + FILEPATH_IMAGE_SUFFIX_BLOCK
		img_clean = FILEPATH_PREFIX + entry[0] + FILEPATH_IMAGE_SUFFIX_CLEAN
		img_block = FILEPATH_PREFIX + entry[0] + FILEPATH_IMAGE_SUFFIX_BLOCK

		website_clean = Website(txt_clean, img_clean, "clean")
		website_block = Website(txt_block, img_block, "block")
		pair = WebsitePair(website_clean, website_block)

		if i == 0:
			print(get_csv_header(website_clean, website_block, pair))

		print(get_csv_string(website_clean, website_block, pair))


def main():
	argument_total = len(sys.argv)
	if argument_total == 1:
		process_manifest()
	elif argument_total == 2:
		process_single_website(sys.argv[1])
	else:
		print("Invalid command line arguments.")
		print("Usage: python3 export_to_csv.py <WEBSITE_URL> ")
		exit()
	

if __name__ == "__main__":
	main()