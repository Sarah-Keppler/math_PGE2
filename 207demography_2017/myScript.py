import sys


with open("country.txt") as f:
    data = f.readlines()
    myList = []
    for line in data:
        myList.append(line[:-1])
    print(myList)
