iFile = open("brainhead.csv", "r+")
oFile = open("brainheadclean.csv", "w+")

for line in iFile:
    splt = line.split()
    strng = ""
    for thing in splt:
        strng = strng + str(thing) + ","
    strng = strng[:-1] + "\n"
    oFile.write(strng)
