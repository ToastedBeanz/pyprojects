# v1.0.1.0

import random
import string

def generate_string(length: int = 16) -> str:
    characters = string.ascii_letters + string.digits # string.ascii_letters has a - z AND A - Z, and string.digits has 0 - 9. 
    
    random_string = ""
    for i in range(length):
        random_string += random.choice(characters) # append a random character to the string
        
    return random_string # return random string

if __name__ == "__main__":
    # Example usage:
    print(generate_string())

# fun fact:
# If there are 62 different characters, and a length of 16, there are exactly 47,672,401,706,823,533,450,263,330,816 different combinations!