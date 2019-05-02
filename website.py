#	Doc Package
#	website.py 
#	
#	Author: Jason Hildreth
#	Research Advisor: Dr. William C. Garrison III
#	University of Pittsburgh
#	Department of Computer Science
#	
#	The Website class stores attributes about a website. A website with no blocker is 
#	referred to as "clean" and a website with a blocker is referred to as "block". 
#	This is to eliminate confusion of terms like "blocker" and "no blocker". 
#
#	The WebsitePair class stores changes in attributes of two website objects, with and
#	without blockers. 


import cv2 
import numpy
import tools_processing_tools as tools


class Website:
	CSV_HEADER = [
		"url",
		"dom length",
		"requests count",
		"logs count",
		"white pixels count",
		"total pixels count",
		"white to total pixels ratio"
	]

	# 24 bit based colors represented as RGB [8, 8, 8] for OpenCV.
	WHITE_PIXEL = [255, 255, 255]
	BLACK_PIXEL = [0, 0, 0]		
	
	CLEAN = "clean"
	BLOCK = "block"
	
	# Enumeration of string copies of parameters.
	URL = 0
	DOM = 1
	REQUESTS = 2
	LOGS = 3
	WHITE_PIXELS = 4
	TOTAL_PIXELS = 5
	WHITE_TO_TOTAL_RATIO = 6
	
	# Parameters of a website
	type = ""
	url = ""
	dom = ""
	requests = []
	logs = []
	white_pixels = 0
	total_pixels = 0
	white_to_total_ratio = 0
	
	parameter_strings = [] # Used for csv exporting
	
	
	def __init__(self, txt_file, img_file, website_type):
		"""Instantiates a website object. 
		   Filepath txt_file: The text file from Biopsy for the website.
		   Filepath img_file: The image file from Biopsy for the website.
		   String type: The type of website, CLEAN or BLOCK. Use the defined
		   				constants of the class as the parameter. 
		   """
		
		self.type = website_type
		
		# Process the .txt file
		txt = open(txt_file)
		entries = txt.readlines()
		url = entries[0]
		
		# Process the DOM, HTTP requests, and console.error() entries. 
		for i in range(1, len(entries)):
			if tools.DOM_TAG in entries[i]:
				self.dom = entries[i]
			elif tools.HTTP_TAG in entries[i]:
				self.requests.append(entries[i])
			elif tools.LOG_TAG in entries[i]:
				self.logs.append(entries[i])
		
		# Process the image file 
		img = cv2.imread(img_file)
		black_boundary = numpy.array(self.BLACK_PIXEL, numpy.uint8)
		white_boundary = numpy.array(self.WHITE_PIXEL, numpy.uint8)
		dst_white = cv2.inRange(img, white_boundary, white_boundary)
		dst_all = cv2.inRange(img, black_boundary, white_boundary)
		self.total_pixels = cv2.countNonZero(dst_all)
		self.white_pixels = cv2.countNonZero(dst_white)
		self.white_to_total_ratio = self.white_pixels / self.total_pixels
		
		# Stores string representations of the attributes for exporting. 
		self.parameter_strings[URL] = self.url 
		self.parameter_strings[DOM] = str(len(self.dom))
		self.parameter_strings[REQUESTS] = str(len(self.requests)) 
		self.parameter_strings[LOGS] = str(len(self.logs))
		self.parameter_strings[WHITE_PIXELS] = str(self.white_pixels)
		self.parameter_strings[TOTAL_PIXELS] = str(self.total_pixels)
		self.parameter_strings[WHITE_TO_TOTAL_RATIO] = str(self.white_to_total_ratio)


	def get_url(self):
		"""Returns the url of the website.
		"""
		return self.url 
		
		
	def get_dom(self):
		"""Returns a string representation of the DOM of the website.
		"""
		return self.dom
		
		
	def get_requests(self):
		"""Returns a list object containing all HTTP requests of the website.
		"""
		return self.requests
		
		
	def get_logs(self):
		"""Returns a list object containing all console.error() entries of the website.
		"""
		return self.logs	
		
		
	def get_white_pixels(self):
		"""Returns the number of white pixels of the website."""
		return self.white_pixels
		
		
	def get_total_pixels(self):
		"""Returns the total number of pixels of the website.
		"""
		return self.total_pixels
		
		
	def get_white_to_total_ratio(self):
		"""Returns the ratio of white / total pixels of the website.
		"""
		return self.white_to_total_ratio 
	
	
	def get_csv_header(self, url_included):
		"""Returns a comma-separated-values header of all the parameters present in the 
		   Website object. 
		   
		   Arguments:
		   	Boolean url_included: If true, includes the url in the string.
		   """
		   
		csv = ""
		if url_included == True:
			csv = CSV_HEADER[0] + ","
		
		for i in range(1, len(CSV_HEADER)):
			csv = csv + CSV_HEADER[i] + " " + type + ","
			
		return csv
		
		
	def to_csv(self, url_included):
		"""Returns a comma-separated-value formatted string of all of the parameters in 
		   the Website object.
		   Arguments: 
		   	Boolean url_included: If true, includes the url in the string.
		   	"""
		   	
		csv = ""
		if url_included == True:
			csv = parameter_strings[0] + ","
			
		for i in range(1, len(parameter_strings)):
			csv = csv + parameter_strings[i] + " " + type + ","
		
		return csv
		
		
class WebsitePair:
	CSV_HEADER = [
		"dom change count",
		"dom change proportion",
		"requests change count",
		"requests change proportion",
		"logs change count",
		"logs change proportion",
		"white pixel change count",
		"white pixel change proportion"
	]
	
	# Enumeration for string copies of parameters.
	DOM_CHANGE_COUNT = 0
	DOM_CHANGE_PROPORTION = 1
	REQUESTS_CHANGE_COUNT = 2
	REQUESTS_CHANGE_PROPORTION = 3
	LOGS_CHANGE_COUNT = 4
	LOGS_CHANGE_PROPORTION = 5
	WHITE_PIXEL_CHANGE_COUNT = 6
	WHITE_PIXEL_CHANGE_PROPORTION = 7

	valid_files = False
	dom_change_count = 0
	dom_change_proportion = 0.0
	requests_change_count = 0
	requests_change_proportion = 0.0
	logs_change_count = 0
	logs_change_proportion = 0.0
	white_pixel_change_count = 0
	white_pixel_change_proportion = 0.0
	
	parameter_strings = []
	
	
	def __init__(self, noblocker, blocker):
		"""Instantiates a WebsitePair object that contains attributes describing changes
		   across the two website objects.
		   """
		if website_noblocker.get_url() == website_blocker.get_url():
			self.valid_files = True
			
		self.dom_change_count = len(noblocker.get_dom()) - len(blocker.get_dom())
		self.dom_change_proportion = len(blocker.get_dom()) / len(noblocker.get_dom())
		
		self.requests_change_count = len(noblocker.get_requests()) - len(blocker.get_requests())
		if len(noblocker.get_requests()) == 0:
			self.requests_change_proportion = 0
		else:
			self.requests_change_proportion = len(blocker.get_requests()) / len(noblocker.get_requests())
		
		self.logs_change_count = len(blocker.get_logs) - len(noblocker.get_logs)
		if len(blocker.get_logs()) == 0:
			self.logs_change_proportion = 0
		else:
			self.logs_change_proportion = len(noblocker.get_logs()) / len(blocker.get_logs())
		
		self.white_pixel_change_count = blocker.get_white_pixels() - noblocker.get_white_pixels()
		if blocker.get_white_pixels() == 0:
			self.white_pixel_change_proportion = 0
		else:
			self.white_pixel_change_proportion = noblocker.get_white_pixels / blocker.get_white_pixels()
		
		self.parameter_strings[DOM_CHANGE_COUNT] = self.dom_change_count
		self.parameter_strings[DOM_CHANGE_PROPORTION] = self.dom_change_proportion
		self.parameter_strings[REQUESTS_CHANGE_COUNT] = self.requests_change_count
		self.parameter_strings[REQUESTS_CHANGE_PROPORTION] = self.requests_change_proportion
		self.parameter_strings[LOGS_CHANGE_COUNT] = self.logs_change_count
		self.parameter_strings[LOGS_CHANGE_PROPORTION] = self.logs_change_proportion
		self.parameter_strings[WHITE_PIXEL_CHANGE_COUNT] = self.white_pixel_change_count
		self.parameter_strings[WHITE_PIXEL_CHANGE_PROPORTION] = self.white_pixel_change_proportion
		
			
	def is_website_pair_valid(self):
		"""Returns true if the website objects are of the same url, false otherwise.
		"""
		return self.valid_files
			
			
	def get_dom_change_count(self):
		"""Returns the difference in dom sizes of clean - block.
		"""
		return self.dom_change_count
		
		
	def get_dom_change_proportion(self):
		"""Returns the ratio of dom sizes of block / clean.
		"""
		return self.dom_change_proportion
		
		
	def get_requests_change_count(self):
		"""Returns the difference in requests of clean - block.
		"""
		return self.requests_change_count
		
		
	def get_requests_change_proportion(self):
		"""Returns the ratio of counts of requests of block / clean.
		"""
		return self.requests_change_proportion
		
		
	def get_logs_change_count(self):
		"""Returns the difference in number of console.error() entries of block - clean.
		"""
		return self.logs_change_count
		
		
	def get_logs_change_proportion(self):
		"""Returns the ratio of counts of console.error() entries of clean / block.
		"""
		return self.logs_change_proportion
		
		
	def get_white_pixel_change_count(self):
		"""Returns the difference in number of white pixels of block - clean.
		"""
		return self.white_pixel_change_count
		
		
	def get_white_pixel_change_proportion(self):
		"""Returns the ratio of white pixels of clean / block.
		"""
		return self.white_pixel_change_proportion
		
		
	def get_csv_header(self):
		"""Returns a comma-separated-values header of all the parameters present in the 
		   Website object.
		   """
		csv = ""
		for i in range(0, len(CSV_HEADER)):
			csv = csv + CSV_HEADER[i] + ","
		return csv
		
		
	def to_csv(self):
		"""Returns a comma-separated-value formatted string of all the parameters in the
		   WebsitePair object.
		   """
		csv = ""
		for i in range(0, len(parameters_string)):
			csv = csv + parameters_string[i] + ","
		return csv