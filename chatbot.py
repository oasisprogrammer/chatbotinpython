# pseudo code

# check input



# match the user given value, 80% match sought
# example
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if age < 0:
        print("Sorry, your response must not be negative.")
        continue
    else:
        break
if age >= 18:
    print("You are able to vote!")
else:
    print("You are not able to vote.")


# Input multiple values from user in one line

x, y = input(), input()

x, y = input().split()

x, y = [int(x), int(y)]

x, y = [int(x) for x in [x, y]]

x, y = [int(x) for x in input().split()]

x, y = map(int, input().split())

#find all close matches of input string from a list

from difflib import get_close_matches

def closeMatches(patterns, word):
    print(get_close_matches(word, patterns))

if __name__ == "__main__":
    word = 'appel'
    patterns = ['ape', 'apple', 'peach', 'puppy']
    closeMatches(patterns, word)
# match keys for input and output
# respond with key of input
# 
# 
# 