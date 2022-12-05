import pprint
with open('input.txt') as temp_file:
    input = [line.rstrip('\n') for line in temp_file]

ls = [["S","P","H","V","F","G"],
      ["M","Z","D","V","B","F","J","G"],
      ["N","J","L","M","G"],
      ["P","W","D","V","Z","G","N"],
      ["B","C","R","V"],
      ["Z","L","W","P","M","S","R","V"],
      ["P","H","T"],
      ["V","Z","H","C","N","S","R","Q"],
      ["J","Q","V","P","G","L","F"]]

for line in input:
    temp = line.split(" ")
    numToMove = int(temp[1])
    fromStack = int(temp[3]) - 1
    toStack = int(temp[5]) - 1

    i = 0
    while i < numToMove:
        element = ls[fromStack].pop(0)
        ls[toStack].insert(i, element)
        i+=1
pprint.pprint(ls)

#part 1
import pprint
with open('input.txt') as temp_file:
    input = [line.rstrip('\n') for line in temp_file]

ls = [["S","P","H","V","F","G"],
      ["M","Z","D","V","B","F","J","G"],
      ["N","J","L","M","G"],
      ["P","W","D","V","Z","G","N"],
      ["B","C","R","V"],
      ["Z","L","W","P","M","S","R","V"],
      ["P","H","T"],
      ["V","Z","H","C","N","S","R","Q"],
      ["J","Q","V","P","G","L","F"]]

for line in input:
    temp = line.split(" ")
    numToMove = int(temp[1])
    fromStack = int(temp[3]) - 1
    toStack = int(temp[5]) - 1

    i = 0
    while i < numToMove:
        element = ls[fromStack].pop(0)
        ls[toStack].insert(0, element)
        i+=1
pprint.pprint(ls)