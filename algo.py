import sys

# need to obtain name

def open_file(filename):
    try:
        f = open(filename, "r")
        return(f, True)
    except:
        print("File open failed: %s" % (filename))
        sys.exit(-1)


def read_whole_file(fd):
    try:
        lines = fd.readlines()
        fd.close()
        # print(lines)
        # Remove newline at end for all
    # https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
        newL = [l for l in lines]
        # print(newL)
        return(newL)
    except:
        print("File read failed")
        sys.exit(-1)

"""

def process_config(lines):
    for l in lines:
        process_line_config(l)

# Process one line of input


def process_line_config(inLine):
    param = inLine.strip().split()
    if param == []:
        pass
    
    elif any(param[0] == word for word in ["JAN", "MAR", "APR"]):
        
        print(param)
    
    else:
        pass
    #print(param)


"""
def td_cc_process_config(lines):
    listA = []
    listB = []
    count = 0
    length = 0
    superlength = len(lines)
    i = 0
    
    while(count < superlength):
        
        if ((lines[count]).strip().split() == []):
            count += 1
        elif any( ((lines[count]).strip().split())[0] == word for word in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]):
            a = lines[count]
            count += 1
            if ((lines[count]).strip().split() == []):
                        count += 1            
            if any( ((lines[count]).strip().split())[0] == word for word in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]): 
                count += 2
                b = lines[count]
                count += 1
                listB += [[a, b]]
                length = len(listB)

        elif (lines[count])[0][0] == "$" or ((lines[count])[0][0] == "-" and (lines[count])[1][0] == "$"):         
            if (i < length -1):
                listB[i] += [lines[count]]
                count += 1
                i += 1
            elif (i < length):
                listB[i] += [lines[count]]
                count += 1
                listA += listB
                listB = []
                i = 0
                length = 0
            else:
                count += 1
        else:
            count += 1
        
    for i in range(len(listA)):   
        print(listA[i])
    
    return listA
                
         

def main(ConfigFile):
    fd, ok = open_file(ConfigFile)
    List = []
    if ok:
        configLines = read_whole_file(fd)
        List = td_cc_process_config(configLines)
    return List

if __name__ == "__main__":
    main()
