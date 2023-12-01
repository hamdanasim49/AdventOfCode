import re
with open('input.txt') as temp_file:
    input = [line.rstrip('\n') for line in temp_file]

sum = 0

#Part 1
"""for line in input:
    first_digit = line[0] if line.isdigit() else next((char for char in line if char.isdigit()), None)
    last_digit = line[-1] if line.isdigit() else next((char for char in reversed(line) if char.isdigit()), None)
    number = (int(first_digit) * 10) + int(last_digit)
    sum += number
"""

#Part 2
DIGITS = "1234567890"
DIGITS_AS_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
for line in input:
    numbers = []
    for i, c in enumerate(line):
        if c in DIGITS:
            numbers.append(int(c))
        for word, digit in DIGITS_AS_WORDS.items():
            if line[i:].startswith(word):
                numbers.append(digit)
                break
    sum += (numbers[0] * 10 + numbers[-1])
    
print(sum)