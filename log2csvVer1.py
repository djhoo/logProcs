import sys
def prcsLine(line):
    print(line)


def main():
    filename = sys.argv[1]
    filename1= filename+".csv"
    fc = open(filename1, "w")
    fc.writelines("curPos,  curSpd,  targSpd, pid"+"\n")
    start = 0
    with open(filename,'r') as f:
        line =f.readline()
        while line:
#            print(line)
            if(line.find("state  curPos  curSpd  targSpd pid") != -1):
                print(line)
                start = 1
            if(start == 1) and (line.find("M31:ENG")!=-1):
                if((line.find("8 ,") != -1) or (line.find("64 ,") != -1)or (line.find("1 ,") != -1)):
#                    print(line)
                    index = line.find("1 ,")
                    if(index != -1):
                        line1 = line[index+3:-1]
                        fc.writelines(line1+"\n")
                    else:
                        index = line.find("8 ,")
                        if(index != -1):
                            line1 = line[index+3:-1]
                            fc.writelines(line1+"\n")
                        else:
                            index = line.find("64 ,")
                            if(index != -1):
                                line1 = line[index+4:-1]
                                fc.writelines(line1+"\n")
                    
                    
            line=f.readline()
    f.close()
    fc.close()
        

main()