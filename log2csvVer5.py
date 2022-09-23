import sys
import pandas as pd
def prcsLine(line):
    print(line)

def atoi(s):
    s = s[::-1]
    num = 0
    for i, v in enumerate(s):
        for j in range(0, 10):
            if v == str(j):
                num += j * (10 ** i)
    return num

def main():
    filename = sys.argv[1]
#    fix1=[1,9 ,8 ,7, 6, 5 ,4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  1,  1,  1]
#    fix2=[1,10,10,10,10,10,10,10,10,10,15,20,30,40,60,70,80,90,100,200,400,800]
    fix1=[1,1,1,1,1,1,1,1,1]
    fix2=[1000,3000,5000,7000,10000,30000,50000,70000,100000]

#    filename1= filename+".csv"
#    fc = open(filename1, "w")
#    fc.writelines("curPos,  curSpd,  targSpd, pid"+"\n")
    start = 0
    fstart = 0
    with open(filename,'r') as f:
        line =f.readline()
        while line:
#            print(line)
            if(line.find("jisstart") != -1):
                if(fstart == 1):
                        fc.close()
                fstart = 1
                index = line.find("j = [")
                name = line[index+5:-2]
                name = int(name)
                name = str(fix1[name])+"%"+str(fix2[name])
                name = name + ".csv"
                fc = open(name, "w")
                fc.writelines("curPos,  curSpd,  targSpd, pid"+"\n")

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