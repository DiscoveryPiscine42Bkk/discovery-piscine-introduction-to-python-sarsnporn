def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}!.")
    else:
        print("Error! itn was not not a name. ")
    
greetings('Trent')
greetings('Aleander')
greetings()
greetings(23)