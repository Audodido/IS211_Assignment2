
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


def processData(file_content):


    person_data = {}                
    split_list = file_content.splitlines()
    format = "%d/%m/%Y" 
    index = 1 

    for i in split_list:
        a = i.decode("utf-8") #decodes each entry
        b = a.split(",") # splits each entry into it's own list
        try:
            date_req_format = datetime.strptime(b[2], format).date() #formats datetime obj
            person_data[b[0]] = (b[1], date_req_format)
        except ValueError:
            LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
            logging.basicConfig(filename = "assignment2.txt",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = "w")
            logger = logging.getLogger()
            logging.error("Error processing line #{} for ID #{}".format(index, b[0]))

        index += 1



    # return dictionary  
    for key, value in person_data.items():
        print(key, ":", value) # return not print
        
        

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



