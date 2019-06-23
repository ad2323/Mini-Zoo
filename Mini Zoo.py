animal = []
cages = {}
def menu():
    print("\n***** WELCOME TO VIRTUAL ZOO *****")
    print("[1] Add Animal")
    print("[2] Create Cage")
    print("[3] Show Animals")
    print("[4] Transfer Animals")
    try:
        x = input()
        x = int(x)
        inputListener(x)
    except:
        print("Invalid input. Please try again.")
        menu()
def inputListener(inputNum):
    if inputNum == 1:
        addAnimal()
    elif inputNum == 2:
        create_cage()
    elif inputNum == 3:
        show_animal()
    elif inputNum == 4:
        print("4")
        menu()
    else:
        print("Input no. is not in the mene. Please try again.")
        menu()
def addAnimal():
    x = len(cages)
    if x == 0:
        print("No cages yet.")
        menu()
    else:
        print("Enter cage no.")
        x = input()
        x = int(x)
        if x in cages:
            print("Enter animals name: ")
            animal_name = input()
            animal.append(animal_name)
            cages[x] = animal
            print("Animal successfully added.")
            menu()
        else:
            print("Cage no. do not exist in the cage.")
            menu()
def create_cage():
    print("Enter cage no.")
    x = input()
    x = int(x)
    if x in cages:
        print("Cage no. already exist.")
        menu()
    else:
        print("Cage successfully created.")
        cages[x] = ""
        menu()
def show_animal():
    for x,y in cages.items():
        print(x,y)
    menu()
menu()
