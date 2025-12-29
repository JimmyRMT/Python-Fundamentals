#Ask user for their name and remove whitespace from str and capitalize user's name
name = input("What's your name? ").strip().title()

#Say hello to user arguments: https://docs.python.org/3/library/functions.html#print
print(f"Hello, {name}")