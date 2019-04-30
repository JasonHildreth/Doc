# Doc
Software package to analyze faults that appear in webpages as a result of content blockers.

## What is Doc? 
Doc is a package containing various tools for collecting and analyzing snapshots of data from website following a two-pass approach. In this approach, website data is collected on the same webpage at the same time, with two instances of the same browser. One with only a collection extension, and the other with a collection extension and a content blocker. 

## Why is it called Doc?
Doc is named as a (punny) metaphor for how a medical doctor diagnoses diseases. Typically, a doctor will examine a patient, take lab samples or document vital signs, and then diagnose an illness or disease. Doc works by examining a website, taking data points from that website, and then attempts to diagnose its faults that resulted from a content blocker. 

## What is the purpose of Doc?
Content blockers such as AdBlock Plus, uBlock Origin, NoScript, etc, attempt to allow us to browse a website and maintain some privacy by blocking invasive analytics and tracking scripts. The more extreme blockers, should one choose to employ, can block Javascript across the board, eliminating most threats to a person's system and privacy. 

Content blockers have the tendency to make a website unusable; especially if the web developers have not taken steps to allow for a clean render when Javascript or other objects fail to produce. In these situations, the user must cease using the website or temporarily disrupt their online protection to use the website. Doc is a part of the bridge to a future solution of that problem. Doc attempts to quantify a broken website. If the website can be deemed "broken", then we could look into a solution that can restore functionality to a website without allowing malicious objects to load. 

## Dependencies and Requirements
- Google Chrome
- Chrome Driver
- Selenium
- Python 3

## Initial Setup
1. Placeholder