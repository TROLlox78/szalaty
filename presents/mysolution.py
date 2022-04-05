# GENERATE DATA:
# from random import *
# file = open('sizes.txt', 'w')
# for i in range(0,150):
#     file.write(f'{randint(1,50)}x{randint(1,50)}x{randint(1,50)}\n')


file = open('sizes.txt', 'r')

def calculatesize(file):
    area=0
    for i in range(0,150):
        line=file.readline().strip().split('x')
        side1=int(line[0])*int(line[1])
        side2=int(line[2])*int((line[0]))
        side3=int(line[2]) * int((line[1]))
        area+=2*(side1)+(2*(side2))+(2*(side3))
    return area
def plottwist(file):
    totalpillow = 0
    for i in range(0, 150):
        ls = []
        line = file.readline().strip().split('x')
        side1 = int(line[0]) * int(line[1])
        side2 = int(line[2]) * int((line[0]))
        side3 = int(line[2]) * int((line[1]))
        ls.append(side1)
        ls.append(side2)
        ls.append(side3)
        pillow=sorted(ls)[::-1][0]
        totalpillow+=pillow
    return totalpillow
# print(calculatesize(file))
print(plottwist(file))