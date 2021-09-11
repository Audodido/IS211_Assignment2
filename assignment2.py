import argparse
import urllib.request
import logging
from datetime import datetime
# from pprint import pprint

def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        data = response.read()
        #print(data)
        return data


# Write a function called ​processData​, which takes the contents of the file as the first parameter, processes 
# the file line by line, and returns a dictionary that maps a person’s ID to a tuple of the form (name, birthday). 
def processData(file_content):
    person_data = {}                
    a_list = file_content.splitlines()
#takes data from url, decodes it from utf to str, stores entries in a list separated by commas—then puts them into a dictionar

    for a in a_list:
        a = a.decode("utf-8")
        b = a.split(",")
        try:
            # print(a)
            format = "%m/%d/%Y" 
            date_req_format = datetime.strptime(b[2], format).date()   
            person_data[b[0]] = (b[1], date_req_format)
            # print(b[0], b[1], date_req_format, b[2])
        except:
            pass
            #print("bad format")



# GOTTA CONVERT THE BDAY IN THE TUPLE TO A  DATETIME OBJECT

    # for value in person_data.values():
    #     try:
    #         format = "%m/%d/%Y"
    #         req_format = datetime.strptime(value[1], format).date()
    #         print(req_format)
    #     except:
    #         pass
    
# return dictionary  
#UNCOMMENT
    for key, value in person_data.items():
        print(key, ":", value)
        
        

# def displayPerson(id, personData):
#     pass

# def main(url):
#     print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    processData(downloadData("https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"))

    # """Main entry point"""
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    # args = parser.parse_args()
    # main(args.url)



