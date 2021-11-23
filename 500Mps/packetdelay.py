import sys
import re
def parseLine(line):
    att = line.split()
    if re.match(r"/NodeList/1/*",att[2]) or att[0] == 'r':
        return None
    
    packetID = line.partition("id")[2].split()[0]
    return (packetID,att[0],att[1])
    
def main():
    args = sys.argv[1:]
    filename = args[0]
    f = open("packet_delay.txt", "w")
    dict = {}
    with open(filename) as file:
        for line in file:
            result =  parseLine(line)
            if result == None:
                continue
            if result[1] == '+':
                dict[result[0]] = result[2]
            else:
                inTime = float(dict[result[0]])
                outTime = float(result[2])
                f.write(str(inTime)+" "+str(outTime-inTime)+"\n")
    f.close()

if __name__ == "__main__":
    main()
