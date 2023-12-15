# Day 8 -Matchsticks

file = open("literals.txt", "r")

allchars = 0
realchars = 0

# Part 1

i = 0
while(i < 300):
    i += 1
    line = file.readline()
    allchars += len(line)-1

    j = 1
    while(j < len(line) - 2):
        realchars += 1
        if(line[j] == '\\'):
            realchars -= 1
            if(line[j+1] == '\\'):
                realchars += 1
                if(line[j-1] == '\\'):
                   realchars -= 1 
                   if(line[j-2] == '\\'):
                       realchars += 1 
            if(line[j-1] != '\\' and line[j+1] == 'x'):
                realchars -= 2
            if(line[j-2] != '\\' and line[j-1] == '\\' and line[j+1] == 'x'):
                realchars -= 2
        j += 1

allchars += 1

file.close()
print("All characters: " + str(allchars))
extras = (int(allchars) - int(realchars))
print("Extra characters: " + str(extras))

# Part 2

file = open("literals.txt", "r")

num = 0
i = 0
while(i < 300):
    i += 1
    line = file.readline()
    
    j = 0
    while(j < len(line)):
        if(line[j] == '\\' or line[j] == '\"'):
            num += 1
        j += 1

# + 600 for 2 new citation marks per line 
print(str(num + 600))
