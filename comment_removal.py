#Start message
print("Remove comments from Python file")
print("-------")

#Input file
f = raw_input("Insert text filename: ")

#Open file
finput = open(f, "r")
foutput = open(f, "w")

#For every line...
for line in finput:
    l = line.split("#")
    l[0] = l[0].replace(" ", "")
    if len(l) > 1:
        l[0] += "\n"
    if l[0].rstrip():
        foutput.write(l[0])
