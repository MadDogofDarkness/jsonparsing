'''
create a simple text based terrain generator
will 
'''
def readfile(filename):
    whitespace = (None, "", " ", "\t", "\r\n", "\n")
    openbrackets = ("{", "[", "(")
    closedbrackets = ("}", "]", ")")
    filetext = ""
    key = ""
    value = ""
    f = open(filename, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        else:
            for word in line:
                for c in word:
                    if c in whitespace:
                        pass
                    elif c in openbrackets:
                        value += c
                    else:
                        
    print(filetext)

if __name__ == ("__main__"):
    args = input("input the filename to read: ")
    readfile(args)

