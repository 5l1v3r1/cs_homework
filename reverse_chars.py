#Import library
import string

#Open file 'abc.txt'
q = open("abc.txt", "r")

### DEFINE LIST
llist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

statistics=[0]

for i in range(25):
    statistics.append(0)

w = []

with open("abc.txt", "r") as q:
    for i in q.read():
        w.append(i)

#convert Upper chars into lower
w = [element.lower() for element in w];
#Take number of appers for each alphabetic char
### RUN LOOP
for i in range(len(w)):
    for j in range(len(llist)):
        if(w[i]==llist[j]):
            statistics[j]=statistics[j]+1
### END LOOP

#Reverse time
i=0
while(i<=len(statistics)):
    if(statistics!=0):
        max=0
        min=i
        break
    else:
        i=i+1

#Spot the characters
for i in range(len(statistics)):
    if((statistics[i]>statistics[max])):
        max=i
    if((statistics[i]<statistics[min])and(statistics[i]!=0)):
        min=i

#Revserse chars
for i in range(len(p)):
    if(w[i]==llist[max]):
        w[i]=llist[min]
    elif(w[i]==llist[min]):
        w[i]=llist[max]
        
### List-to-string conversion

w = ''.join(w)

#Print the final output
print(w.upper())
