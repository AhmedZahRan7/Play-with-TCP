import sys
import re
def parseLine(line):
    att = line.split()
    if re.match(r"/NodeList/1/*",att[2]):
        return None
    x = 0
    if att[0] == '-':
        x=-1
    if att[0] == '+':
        x=1
    return (x,att[1])
    
def main():
    args = sys.argv[1:]
    filename = args[0]
    f = open("queue_time.txt", "w")
    n = 0
    with open(filename) as file:
        for line in file:
            result =  parseLine(line)
            if result == None or result[0]==0:
	            continue
            n += result[0]
            t = result[1]
            f.write(""+str(t)+" "+str(n)+"\n")
    f.close()

if __name__ == "__main__":
    main()
