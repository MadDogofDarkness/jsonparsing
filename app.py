'''
json reader
'''
def readfile(filename):
    whitespace = (None, "", " ", "\t", "\r\n", "\n")
    openbrackets = ("{", "[", "(")
    closedbrackets = ("}", "]", ")")
    delimiter = (':', ',')
    title = "JSON"
    newtitle = ""
    filetext = ""
    key = ""
    value = ""
    state = "reading"
    f = open(filename, 'r')
    print(f"---------------{title}-----------------")
    while True:
        line = f.readline()
        if not line:
            break
        else:
            for word in line:
                for c in word:
                    #print(f"{state} : {c}") # debug
                    #gets the char from each word
                    if c in whitespace:
                        pass
                    elif c == openbrackets[0]:
                        state = "readingkey"
                        if title != newtitle:
                            title = newtitle
                            print(f"---------------{title}-----------------")
                    elif c == openbrackets[1]:
                        state = "readingtitle"
                        newtitle = ""
                    elif c == closedbrackets[0]:
                        state = "reading"
                        print(f"{key}   : {value} ")
                        key = ""
                        value = ""
                    elif c == delimiter[0]:
                        state = "readingvalue"
                    elif c == delimiter[1]:
                        state = "readingkey"
                        print(f"{key}   : {value} ")
                        key = ""
                        value = ""
                    else:
                        if state == "readingkey":
                            key += c
                        elif state == "readingvalue":
                            value += c
                        elif state == "readingtitle":
                            newtitle += c
                        else:
                            pass
                        
    #print(filetext)

if __name__ == ("__main__"):
    filename = input("input the filename to read: ")
    readfile(filename)

