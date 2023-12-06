#Day 1 -Apartment Levels

file = open('Levels.txt', 'r')

Level = 0
n = 0

while 1:
    n += 1
    # read by character
    char = file.read(1)
    if char == '(':
        Level += 1
        
    if char == ')':
        Level -= 1

    if Level == -1:
        print(n)

    if not char: 
        break

print(Level)
 
file.close()