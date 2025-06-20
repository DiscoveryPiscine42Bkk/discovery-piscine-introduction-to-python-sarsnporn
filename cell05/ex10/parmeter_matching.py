import sys

params = sys.argv[1:]

if len(params) != 1:
    print("none")
else:
    user:input = input("What was the keyword? ")
    if user_input == params[0]:
        print("Good job!")
    else:
        print("Nope, sorry...")