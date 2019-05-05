# Doc
Software package to analyze faults that appear in webpages as a result of content blockers.

Doc was built and used for research by Jason Hildreth under the research advisement of Dr. Garrison of the Computer Science department at the University of Pittsburgh. 

## What is Doc? 
Doc is an open source package containing various tools for collecting and analyzing snapshots of data from website following a two-pass approach. In this approach, website data is collected on the same webpage at the same time, with two instances of the same browser. One with only a collection extension, and the other with a collection extension and a content blocker. 

## Why the name "Doc"?
Doc is named as a (punny) metaphor for how a medical doctor diagnoses diseases. Typically, a doctor will examine a patient, take lab samples or document vital signs, and then diagnose an illness or disease. Doc works by examining a website, taking data points from that website, and then attempts to diagnose its faults that resulted from a content blocker. The various tools of Doc are named as metaphors to the field of medicine.

## What is the purpose of Doc?
Content blockers such as AdBlock Plus, uBlock Origin, NoScript, etc, attempt to allow us to browse a website and maintain some privacy by blocking invasive analytics and tracking scripts. The more extreme blockers, should one choose to employ, can block Javascript across the board, eliminating most threats to a person's system and privacy. 

Content blockers have the tendency to make a website unusable; especially if the web developers have not taken steps to allow for a clean render when Javascript or other objects fail to produce. In these situations, the user must cease using the website or temporarily disrupt their online protection to use the website. Doc is a part of the bridge to a future solution of that problem. Doc attempts to quantify a broken website. If the website can be deemed "broken", then we could look into a solution that can restore functionality to a website without allowing malicious objects to load. 

## Dependencies and Requirements
- Google Chrome
- Chrome Driver
- Python 3
- Selenium for Python 3
- OpenCV for Python 3
- NumPy for Python 3

Anaconda is optional, but allows for much simpler installation of the OpenCV and NumPy libraries. 

## Doc Components
Doc is built from three primary utilities along with smaller utilities that are more literal in name than the primary metaphorical counterparts. 

### Scalpel
Scalpel is the blade of Doc. It works by "opening up" Chrome and allowing access to some inner sections. Scalpel is a Chrome extension written in Javascript. For security purposes, Javascript has no I/O. To get around this limitation, Scalpel places data that could be useful in research into the ```console.error()``` log. 

### Biopsy
Biopsy is the sample collection of Doc. While Biopsy's name is hidden as a collection tool, it actually operates Chrome through automation. Biopsy can not work with Scalpel, and Scalpel provides no tangible benefit without Biopsy. Biopsy is written in Python and makes use of the Selenium browser automation library. 

### Diagnose
Diagnose is the detector of Doc. It works by taking in samples created by Biopsy, and can output a detected fault. Diagnose is written in Python and uses the OpenCV and NumPy libraries. 

#### Tools
- ```text_processing_tools.py``` contains constants and functions use to manage and process data coming out of the ```console.error()``` log and transform them into more user-friendly data. 
- ```export_to_csv.py``` exports either a single website's parameters as a CSV string, or an entire manifest of data. If executed with no command line arguments, the entire manifest will be exported as a CSV string. If executed with a website string, it will export that single website as a CSV string. 
- ```config.py``` contains the necessary paths for Selenium Chrome profiles and other system values. 
- ```manifest.py``` contains a list that stores websites.  


## Initial Setup
This repository comes with all files necesasary to execute Doc. The user is only responsible for making sure they have the above the dependencies and modifying the appropriate configurations. 

1. Ensure Chromedriver is in the correct place for your system variables. 
2. Create two Chrome profiles, one for the test with no blocker, and one with. 
3. Open ```config_template.py``` and store the working paths of these Chrome profiles inside this template. Chrome profile paths can be found by navigating to ```Chrome://version``` within Chrome. Save as ```config.py```.
4. Run the ```build_profiles.py``` script and follow the instructions. This will provide the package with two profiles that are configured properly for the two-pass analysis technique. 


## Using Doc
Since this package was written for research purposes, it has multiple scripts for collecting data, formatting data, and diagnosing data. It is designed this way to allow for additional fault detectors to be built in. 

A typical examination will be a run of Biopsy. Diagnose can then be used to test if detection heuristics are accurate or the data can be exported CSV for examination. 

Doc currently supports detection of the following website faults:
- Page is blank when using NoScript or Scriptsafe. 

Works in progress:
- Audio Players not visible when using NoScript or Scriptsafe. 
