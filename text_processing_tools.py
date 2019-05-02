#   Doc Package
#   build_profiles.py
#   
#   Author: Jason Hildreth
#   Research Advisor: Dr. William C. Garrison III
#   University of Pittsburgh
#   Department of Computer Science
#
#   These tools are used to aid in analysis and processing of strings for Doc. Due to the
#   nature of the research, new constants and functions must be added. This volatility 
#   means that great care must be taken with constants such as the CSV_HEADER. Depending
#   on data used, it will need to be modified. 
#   
#   Future work will be a re-work of this file to allow the CSV_HEADER to be built 
#   from the config file. 


import json


CSV_HEADER = ["page is blank?,", "DOM Size Clean,", "DOM Size Block,", "DOM Size Change,", 
"DOM Percent Change,", "HTTP Clean,", "HTTP Block,", "HTTP Count Change,", 
"HTTP Percent Change,", "Log Clean,", "Log Block,", "Log Count Change,", 
"Log Percent Change,", "Total Pixels Clean,", "White Pixels Clean,", 
"White Pixels to Total Ratio Clean,", "Total Pixels Block"]


# Formatting Constants
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

FILEPATH_PREFIX = "files/"
FILEPATH_TEXT_SUFFIX_CLEAN = "_clean.txt"
FILEPATH_TEXT_SUFFIX_BLOCK = "_block.txt"
FILEPATH_IMAGE_SUFFIX_CLEAN = "_clean.png"
FILEPATH_IMAGE_SUFFIX_BLOCK = "_block.png"


# Formatting Functions
def strip_JSON(entry):
    """ This function should only be used when you have no way of knowing what
        type of entry you have. It will differentiate and output with the
        correct tag. 
        """
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
        entry without an identifying tag. 
        """
    stripped_entry = ""
    split_first_section = entry.split(HTTP_DELIM_1)
    split_second_section = split_first_section[1].split(HTTP_DELIM_2)
    stripped_entry = split_second_section[0]

    return stripped_entry


def strip_log_entry(entry):
    """ Removes console log JSON format off of a log entry. Returns the entry 
        without an identifying tag. 
        """
    stripped_entry = ""
    split_entry = entry.split(LOG_DELIM_1)
    for i in range(0, len(split_entry)):
        if LOG_DELIM_2 in split_entry[i]:
            split_entry_again = split_entry[i].split(LOG_DELIM_2)
            stripped_entry = split_entry_again[0]

    return stripped_entry


def strip_DOM(dom):
    """ Removes the console.log JSON format from a DOM entry. Returns the entry
        without an identifying tag. 
        """
    stripped_dom = ""

    dom_string = json.dumps(dom)

    first_split = dom_string.split(DOM_DELIM_1)
    second_split = first_split[1].split(DOM_DELIM_2)
    stripped_dom = second_split[0]

    return stripped_dom


def format_DOM_to_JSON(dom):
    """ Takes a single line string of a DOM collected by Biopsy and returns
        a multi-line, easier-to-view string. The parameter must be a string
        and not a dict object. 
        
        WARNING: THIS FUNCTION IS NOT COMPLETE. 
        """
    formatted_dom = dom.replace(DOM_FORMAT_REMOVE_1, "")
    
    return formatted_dom