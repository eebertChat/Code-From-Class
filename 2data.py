
def movie_data(filename):
    '''
    Purpose: To process a file and return a list of lists containing the
    two-dimensional data from the file. 

    Assumption: The file is in csv (comma seperated values). There is only one 
    header row and the data begins directly after.

    Parameters: The file name that needs to be processed; str

    Return Value: A list of lists containing the 2d data
    '''

    movie_data = []

    fd = open(filename, 'r')

    fd.readline()   # Skip the header row in the file

    for line in fd:         # line is a string from the file
        line = line.strip().split(",")      # We've split the line on commas and is now a list
        
        for i in range(1,3):
            line[i] = float(line[i])

        line[3] = int(line[3])
        line[4] = float(line[4])

        for i in range(6,8):
            line[i] = float(line[i])

        movie_data.append(line)

    fd.close()

    return movie_data


if __name__ == "__main__":
    holiday_movies = movie_data("holiday_movie_sales.csv")

    # If I want to print the 3rd row
    print(holiday_movies[2])

    # If I want to print the #1 movie of the holiday from the 3rd row
    print(holiday_movies[2][5])

    # If I want to print the #1 movie from the Halloween holiday
    print(holiday_movies[7][5])

    for row in holiday_movies:
        if(row[0]=="Halloween"):
            print(row[5])