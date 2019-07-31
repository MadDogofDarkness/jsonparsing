'''
as it reads, needs to structure the data for output
should output each line by line, 
 with one property or key per line
indent to show sub keys and sub properties

to do this, the method needs the line to read
 and the current level of indent
'''
def parseline(line, indent):
    #
    # should iterate through the line
    # 
    #


'''
needs to read data, we can start line by line

to do this the method needs the file and the end of line char
'''

def readdata(filename, end_of_line):
    # print out each line of converted json
    # in a nice format
    #
    # -------------object header---------------
    # key : value
    # property :
    #          : subkey : value
    #
    # read everything in as strings
    # no point in converting since just displaying data
    # maybe add it in later

'''
needs to handle os excecptions from files

'''

def openfile():
    # will return the file once checked for excecptions
    # determines the os for endline char?
    # open file
    # if osexcecption
    # return "an error occurred attempting to access the file :("
    # else return file for reading