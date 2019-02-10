##DEFINE FUNCTION##
#Define binary search
def bis(alpha, target):
    lower = 0
    upper = len(alpha)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = alpha[x]
        if(target == val):
            return x
        elif (target > val):
            if(lower == x):
                break #Break out of condition
            lower = x
        elif(target < val):
            upper = x


#Define list of defaults elements
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

statistics=[0]
#Begin loop
for i in range(25):
    statistics.append(0)
print(len(alpha),len(statistics))
lines=input()
doesnotmatter=len(lines)
for i in range(doesnotmatter):
    target=bis(alpha, lines[i])
    statistics[target]=statistics[target]+1

#Get Max and Min
#CHECK: each letter, appears at least once in the txt file
for i in range(25):
    if(statistics[i]>statistics[i+1]):
        maxl=alpha[i]
    if(statistics[i]<statistics[i+1]):
        if((statistics[i]!=0) and (statistics[i+1]!=0)):
            minl=alpha[i]

#Reverse loop
for i in range(doesnotmatter):
    if(maxl==lines[i]):
        lines[i]==minl
    if(minl==lines[i]):
        lines[i]==maxl

#Output lines
print(lines)

#Repeat 25 times
for i in range(25):
    print(alpha[i], statistics[i])
