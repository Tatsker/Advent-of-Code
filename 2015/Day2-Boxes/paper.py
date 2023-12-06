#Day 2 -Box Dimensions


file = open('objects.txt', 'r')

n = 0
xy = 0
yz = 0
zx = 0
fullSize = 0

while 1:
    n += 1
    # read by line
    Dimensions = file.readline().split('x')
    print(fullSize)

    if not Dimensions[0]: 
        break

    x = Dimensions[0]
    y = Dimensions[1]
    z = Dimensions[2]

    xy = 2*int(x)*int(y)
    yz = 2*int(y)*int(z)
    zx = 2*int(z)*int(x)

    fullSize += xy + yz + zx + min(xy, yz, zx)/2


print(fullSize)


file.close()