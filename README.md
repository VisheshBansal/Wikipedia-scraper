# Wikipedia Page Scraper

A PyPackage that scraps data from Wikipedia pages and stores data in an object.

## Import project

''' from Wikipediapagescrapper import pagescrapper '''

## Create Scrapped page

''' WikiPage = pagescrapper.scrapWikipediaPage(topicname) '''

## Get a list of subsections

''' print(WikiPage.section_names) '''

## Get text stored in section

''' WikiPage.text '''

## Get subsection object

''' subsection = Wikipage.getSection(section_name)

