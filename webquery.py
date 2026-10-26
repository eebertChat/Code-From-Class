import urllib.request as web
import os.path

FILENAME = "recall_data.xml"

if (not os.path.isfile(FILENAME)):
    url = "https://www.fda.gov/media/191968/download?attachment"
    webpage = web.urlopen(url)
    xml_data = webpage.read()

# Files have three different modes:
# 'r' - read only (the file has to exist for this to work)
# 'w' - write (if the file doesn't exist it will be created. If it does exist it
# will be overwritten)
# 'a' - append (if the file doesn't exist it will be created. If it does exist
# new data will be appended to the end of the file)

    fd = open(FILENAME, 'wb')     #Open a file for writing
    fd.write(xml_data)
    fd.close()      # You have to close a file to make sure everything in the 
                    # buffer got saved.l

else:
    fd = open(FILENAME, "r")

# print(webpage.readline().decode('utf-8'))

#for _ in range(20):                 # _ we don't need the counter so
#    print(webpage.readline().decode('utf-8'))

line = ""

# Ignore any header information that exists
while line[:14] != "<recallsdata>":
    line = webpage.readline()
    line = line.decode("utf-8")         # Decodes byte stream to utf-8

productNum = 1

line = webpage.readline()       # This is the first recall item
line = line.decode("utf-8")

while line[:14] != "</recallsdata>":    # While there are recalls to process
    print(productNum)

    while line[:10] != "</recalls>":
        print(line.rstrip())            # lstrip / rstrip are one-sided whitespace removal
        line = webpage.readline()
        line = line.decode("utf-8")
    print(line.rstrip())

    productNum += 1

    line = webpage.readline()
    line = line.decode("utf-8")

fd.close()