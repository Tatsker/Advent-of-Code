#Day 5 -Naughty strings

# Part 1
file = open('strings.txt', 'r')

num = 0
i = 0
while(i < 1000):
    string = file.readline()
    i += 1
    if string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u") > 2:
        if string.rfind("ab") == -1 and string.rfind("cd") == -1 and string.rfind("pq") == -1 and string.rfind("xy") == -1:
            if string.rfind("aa") != -1 or string.rfind("bb") != -1 or string.rfind("cc") != -1 or string.rfind("dd") != -1 or string.rfind("ee") != -1 or string.rfind("ff") != -1 or string.rfind("gg") != -1 or string.rfind("hh") != -1 or string.rfind("ii") != -1 or string.rfind("jj") != -1 or string.rfind("kk") != -1 or string.rfind("ll") != -1 or string.rfind("mm") != -1 or string.rfind("nn") != -1 or string.rfind("oo") != -1 or string.rfind("pp") != -1 or string.rfind("qq") != -1 or string.rfind("rr") != -1 or string.rfind("ss") != -1 or string.rfind("tt") != -1 or string.rfind("uu") != -1 or string.rfind("vv") != -1 or string.rfind("ww") != -1 or string.rfind("xx") != -1 or string.rfind("yy") != -1 or string.rfind("zz") != -1:
                num += 1
                print(num)
file.close()

# Part 2
file = open('strings.txt', 'r')

num = 0
i = 0
while(i < 1000):
    string = file.readline()
    i += 1
    j = 0
    switch = 0

    while(j < 13):
        k = j + 2
        while(k < 15):
            if(string[j] + string[j+1] == string[k] + string[k+1]):
                switch = 1
                break
            k += 1
        if(switch == 1):
            break
        j += 1
    j = 0

    if(switch == 1):
        while(j < 14):
            if(string[j] == string[j+2]):
                num += 1
                print(num)
                print(string)
                break
            j += 1

file.close()