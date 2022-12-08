import pprint
with open('input.txt') as temp_file:
    input = [line.rstrip('\n') for line in temp_file]

dirs = {}
dir_queue = []
for line in input:
    temp = line.split(' ')
    if temp[1] == 'cd' and temp[2] != '..':
        dir = temp[2]
        dirs["".join(dir_queue) + dir] = 0
        dir_queue.append("".join(dir_queue) + dir)
    elif "$ cd .." in line:
        dir_queue.pop()
    elif line[0].isdigit():
        for dir in dir_queue:
            dirs[dir] += int(temp[0])
            
print(dirs)
unused_space = 30000000 - (70000000 - dirs["/"])
print(unused_space)
answer_one = sum(dirs[dir] if dirs[dir] <= 100000 else 0 for dir in dirs)
answer_two = min(dirs[dir] for dir in dirs if unused_space <= dirs[dir])
print("p1:", answer_one)
print("p2:", answer_two)