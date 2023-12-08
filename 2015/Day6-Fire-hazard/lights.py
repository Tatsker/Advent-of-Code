# Day 6 -Fire hazard

file = open("instructions.txt", "r")
lights = [ [0] * 1000 for _ in range(1000)]

# Part 1

i = 0
while(i < 300):
    i += 1
    instruction = file.readline()

    if(instruction.startswith("toggle")):
        words = instruction.split()
        start = words[1].split(",")
        stop = words[3].split(",")
        x1 = int(start[0])
        y1 = int(start[1])
        x2 = int(stop[0])
        y2 = int(stop[1])

        if(x1 < x2):
            while(x1 <= x2):
                if(lights[x1][y1] == 0):
                    lights[x1][y1] = 1
                else:
                    lights[x1][y1] = 0

                while(y1 < y2):
                    y1 += 1
                    if(lights[x1][y1] == 0):
                        lights[x1][y1] = 1
                    else:
                        lights[x1][y1] = 0

                while(y1 > y2):
                    y1 -= 1
                    if(lights[x1][y1] == 0):
                        lights[x1][y1] = 1
                    else:
                        lights[x1][y1] = 0
                y1 = int(start[1])
                x1 += 1
        else:
            while(x1 >= x2):
                if(lights[x1][y1] == 0):
                    lights[x1][y1] = 1
                else:
                    lights[x1][y1] = 0

                while(y1 < y2):
                    y1 += 1
                    if(lights[x1][y1] == 0):
                        lights[x1][y1] = 1
                    else:
                        lights[x1][y1] = 0

                while(y1 > y2):
                    y1 -= 1
                    if(lights[x1][y1] == 0):
                        lights[x1][y1] = 1
                    else:
                        lights[x1][y1] = 0
                y1 = int(start[1])
                x1 -= 1

    if(instruction.startswith("turn on") or instruction.startswith("turn off")):
        words = instruction.split()
        start = words[2].split(",")
        stop = words[4].split(",")
        x1 = int(start[0])
        y1 = int(start[1])
        x2 = int(stop[0])
        y2 = int(stop[1])
        if(instruction.startswith("turn on")):
            if(x1 < x2):
                while(x1 <= x2):
                    lights[x1][y1] = 1

                    while(y1 < y2):
                        y1 += 1
                        lights[x1][y1] = 1

                    while(y1 > y2):
                        y1 -= 1
                        lights[x1][y1] = 1
                    y1 = int(start[1])
                    x1 += 1
            else:
                while(x1 >= x2):
                    lights[x1][y1] = 1

                    while(y1 < y2):
                        y1 += 1
                        lights[x1][y1] = 1

                    while(y1 > y2):
                        y1 -= 1
                        lights[x1][y1] = 1
                    y1 = int(start[1])
                    x1 -= 1
        else:
            if(x1 < x2):
                while(x1 <= x2):
                    lights[x1][y1] = 0

                    while(y1 < y2):
                        y1 += 1
                        lights[x1][y1] = 0

                    while(y1 > y2):
                        y1 -= 1
                        lights[x1][y1] = 0
                    y1 = int(start[1])
                    x1 += 1
            else:
                while(x1 >= x2):
                    lights[x1][y1] = 0

                    while(y1 < y2):
                        y1 += 1
                        lights[x1][y1] = 0

                    while(y1 > y2):
                        y1 -= 1
                        lights[x1][y1] = 0
                    y1 = int(start[1])
                    x1 -= 1

num = 0
i = 0
j = 0
while (i < 999):
    i+=1
    while (j < 999):
        j+=1
        if (lights[i][j] > 0):
            num+=1
    j = 0

print(num)
file.close()

# Part 2

lights2 = [ [0] * 1000 for _ in range(1000)]
file = open("instructions.txt", "r")

i = 0
while(i < 300):
    i += 1
    instruction = file.readline()

    if(instruction.startswith("toggle")):
        words = instruction.split()
        start = words[1].split(",")
        stop = words[3].split(",")
        x1 = int(start[0])
        y1 = int(start[1])
        x2 = int(stop[0])
        y2 = int(stop[1])

        if(x1 < x2):
            while(x1 <= x2):
                lights2[x1][y1] += 2

                while(y1 < y2):
                    y1 += 1
                    lights2[x1][y1] += 2

                while(y1 > y2):
                    y1 -= 1
                    lights2[x1][y1] += 2
                y1 = int(start[1])
                x1 += 1
        else:
            while(x1 >= x2):
                lights2[x1][y1] += 2

                while(y1 < y2):
                    y1 += 1
                    lights2[x1][y1] += 2

                while(y1 > y2):
                    y1 -= 1
                    lights2[x1][y1] += 2
                y1 = int(start[1])
                x1 -= 1

    if(instruction.startswith("turn on") or instruction.startswith("turn off")):
        words = instruction.split()
        start = words[2].split(",")
        stop = words[4].split(",")
        x1 = int(start[0])
        y1 = int(start[1])
        x2 = int(stop[0])
        y2 = int(stop[1])
        if(instruction.startswith("turn on")):
            if(x1 < x2):
                while(x1 <= x2):
                    lights2[x1][y1] += 1

                    while(y1 < y2):
                        y1 += 1
                        lights2[x1][y1] += 1

                    while(y1 > y2):
                        y1 -= 1
                        lights2[x1][y1] += 1
                    y1 = int(start[1])
                    x1 += 1
            else:
                while(x1 >= x2):
                    lights2[x1][y1] += 1

                    while(y1 < y2):
                        y1 += 1
                        lights2[x1][y1] += 1

                    while(y1 > y2):
                        y1 -= 1
                        lights2[x1][y1] += 1
                    y1 = int(start[1])
                    x1 -= 1
        else:
            if(x1 < x2):
                while(x1 <= x2):
                    if(lights2[x1][y1] > 0):
                        lights2[x1][y1] -= 1

                    while(y1 < y2):
                        y1 += 1
                        if(lights2[x1][y1] > 0):
                            lights2[x1][y1] -= 1

                    while(y1 > y2):
                        y1 -= 1
                        if(lights2[x1][y1] > 0):
                            lights2[x1][y1] -= 1
                    y1 = int(start[1])
                    x1 += 1
            else:
                while(x1 >= x2):
                    if(lights2[x1][y1] > 0):
                        lights2[x1][y1] -= 1

                    while(y1 < y2):
                        y1 += 1
                        if(lights2[x1][y1] > 0):
                            lights2[x1][y1] -= 1

                    while(y1 > y2):
                        y1 -= 1
                        if(lights2[x1][y1] > 0):
                            lights2[x1][y1] -= 1
                    y1 = int(start[1])
                    x1 -= 1

num = 0
i = 0
j = 0
while (i < 999):
    i+=1
    while (j < 999):
        j+=1
        if (lights2[i][j] > 0):
            num += lights2[i][j]
    j = 0

print(num)
file.close()