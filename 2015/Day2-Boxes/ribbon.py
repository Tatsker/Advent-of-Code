#Day 2 -Ribbon length


file = open('objects.txt', 'r')

n = 0
x = 0
y = 0
z = 0
fullLength = 0

while 1:
    n += 1
    # read by line
    Dimensions = file.readline().split('x')
    print(fullLength)

    if not Dimensions[0]: 
        break

    x = int(Dimensions[0])
    y = int(Dimensions[1])
    z = int(Dimensions[2])

    length = 2*min(x, y, z) + 2*min(max(x,y),max(y,z),max(x,z)) + x*y*z
    fullLength += length

    print(length)


file.close()