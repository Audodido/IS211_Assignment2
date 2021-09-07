import argparse
import urllib.request
import logging
import datetime
from pprint import pprint

def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return data

# Write a function called ​processData​, which takes the contents of the file as the first parameter, processes 
# the file line by line, and returns a dictionary that maps a person’s ID to a tuple of the form (name, birthday). 
def processData(file_content):
    pass


# def displayPerson(id, personData):
#     pass

# def main(url):
#     print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    downloadData("https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv")

    # """Main entry point"""
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    # args = parser.parse_args()
    # main(args.url)




# do two things: write an output file 
# recording which lines in the file ​cannot​ be processed correctly due to an improperly formatted date; and 
# allow a user to enter in an ID number and print out that person’s information. 

#use urllib for getting data from csv
#use datetime for formatting b-days
#use logging to record lines in the file ​cannot​ be processed correctly
#use argparse to let somsone enter id number when program is excecuted from CLI
