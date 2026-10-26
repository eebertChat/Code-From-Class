import urllib.request as web

url = "https://www.fda.gov/media/191968/download?attachment"

webpage = web.urlopen(url)

# Files have three different modes:
# 'r' - read only (the file has to exist for this to work)
# 'w' - write (if the file doesn't exist it will be created. If it does exist it
# will be overwritten)
# 'a' - append (if the file doesn't exist it will be created. If it does exist
# new data will be appended to the end of the file)

# fd = open("recall_data.xml", 'w')     #Open a file for writing

# fd.close()      # You have to close a file to make sure everything in the 
                # buffer got saved.

# print(webpage.readline().decode('utf-8'))

#for _ in range(20):                 # _ we don't need the counter so
#    print(webpage.readline().decode('utf-8'))



line = ""

# Ignore any header information that exists
while(line != "<recallsdata>"):
    line = webpage.readline()
    print(repr(line))
    line = line.decode("utf-8").strip()

line = webpage.readline()
line = line.decode("utf-8").rstrip()
print(line)

webpage.close()