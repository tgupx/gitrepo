# Example of "match-case"

name = input("What's you name? ")

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffndor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Ravenclaw")
