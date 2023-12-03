with open('input.txt') as temp_file:
    input = [line.rstrip('\n') for line in temp_file]
    
sum = 0
#Part 1
"""
for line in input:    
    part = line.split(':')
    game_num = int(part[0].split(' ')[1])
    game = part[1]
    sets = game.split(';')
    flag = True
    for one_set in sets:
        marbles = one_set.split(',')
        for marble in marbles:
            temp = marble[1:]
            temp = temp.split(' ')
            if temp[1] == 'blue':
                blue_count = int(temp[0])
                if blue_count > 14:
                    flag = False
            elif temp[1] == 'red':
                red_count = int(temp[0])
                if red_count > 12:
                    flag = False
            else:
                green_count = int(temp[0])
                if green_count > 13:
                    flag = False
    
    if flag:
        sum += game_num
"""


for line in input:    
    max_red = 0
    max_blue = 0
    max_green = 0
    
    part = line.split(':')
    game_num = int(part[0].split(' ')[1])
    game = part[1]
    sets = game.split(';')
    for one_set in sets:
        marbles = one_set.split(',')
        for marble in marbles:
            temp = marble[1:]
            temp = temp.split(' ')
            if temp[1] == 'blue':
                blue_count = int(temp[0])
                if blue_count > max_blue:
                    max_blue = blue_count
            elif temp[1] == 'red':
                red_count = int(temp[0])
                if red_count > max_red:
                    max_red = red_count
            else:
                green_count = int(temp[0])
                if green_count > max_green:
                    max_green = green_count
    
    print(max_green, max_red, max_blue)
    sum += (max_green * max_red * max_blue)
print(sum)