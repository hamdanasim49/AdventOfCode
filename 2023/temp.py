import re

def find_first_and_last_digit(s):
    # Dictionary mapping spelled-out digits to numerical digits
    digit_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    # Extract all digits, whether numerical or spelled-out
    digits = re.findall(r'\d+|[a-zA-Z]+', s)
    
    # Convert spelled-out digits to numerical digits
    digits = [digit_mapping.get(d, d) for d in digits]
    
    # Find the first and last digit
    first_digit = digits[0] if digits else None
    last_digit = digits[-1] if digits else None
    
    return first_digit, last_digit

# Example usage
example_input = "fivethreeonezblqnsfk1"
first_digit, last_digit = find_first_and_last_digit(example_input)
print(f"For '{example_input}', first digit: {first_digit}, last digit: {last_digit}")
