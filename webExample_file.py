import os.path
import re
import urllib.request as web

url = "https://www.fda.gov/media/191968/download?attachment"

if (not os.path.isfile("recall_data.xml")):
    # Get the XML data from the website
    webpage = web.urlopen(url)
    xml_data = webpage.read()       # It will read this as a byte stream

    # 'wb' for write bytes - we'll overwrite any existing file with the same name
    # fd - file device object
    fd = open("recall_data.xml", 'wb')
    fd.write(xml_data)
    fd.close()


xml_file = open("recall_data.xml", "r")     # Open the file to read as text
out_file = open("recalls.txt", "w")

line = ""

# Ignore the header data in the XML file
while(line != "<recallsdata>"):
    line = xml_file.readline().strip()

productNum = 1

while(line != "</recallsdata>"):

    out_file.write(f"Product {productNum}: \n")

    while(line != "</recalls>"):
        line = xml_file.readline().strip()

        matches = re.search(r'<(\w+)>(.*?)</\1>', line)      #Regex to recognize <Brand>

        if(matches != None and matches.group(1) in ["Brand", "Company", "Date"]):
            out_file.write(f"\t {matches.group(1)}: {matches.group(2).replace("&amp;", "&")} \n")

    productNum += 1

    line = xml_file.readline().strip()
    

xml_file.close()
out_file.close()

# Goal: To print out the recall data in the following format:
# Product <number>:
#   Brand: 
#   Company: 
#   Date: 


# An Exercise for you:
# Change this program to save the processed data to an output file 
# called recalls.txt instead of printing it to the console.

# out = open("recalls.txt", "w")
# out.write(line)



