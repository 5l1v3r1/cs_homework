#Start message
print("Remove comments from Python file")
print("-------")

#Input file
f = raw_input("Insert file name or path: ")

#Open file
finput = open(f, "r")
foutput = open("saida.txt", "w")

#For every line...
for line in finput:
    l = line.split("#")
    l[0] = l[0].replace(" ", "")
    if len(l) > 1:
        l[0] += "\n"
    if l[0].rstrip():
        foutput.write(l[0])