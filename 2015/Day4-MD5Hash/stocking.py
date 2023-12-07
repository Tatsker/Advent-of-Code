#Day 4 -Perfect stocking

import hashlib

key = "bgvyzdsv"
num = 0

#Part 1
while(hashlib.md5((key + str(num)).encode('utf-8')).hexdigest().startswith("00000") != True):
    num += 1
print(num)

#Part 2
while(hashlib.md5((key + str(num)).encode('utf-8')).hexdigest().startswith("000000") != True):
    num += 1
print(num)