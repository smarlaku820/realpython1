from capitals import capitals_dict
from random import choice

if __name__ == "__main__":
    while True:
        state = choice(list(capitals_dict))
        capital = input("capital city of {} is :".format(state))
        if capital.upper() == capitals_dict[state].upper():
            print("Correct")
        elif capital.upper() == 'EXIT':
            print("capital city of {} is {}".format(state, capitals_dict[state]))
            print("Goodbye")
            break