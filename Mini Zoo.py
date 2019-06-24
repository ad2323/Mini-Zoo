animals = [] #NO USE ACTUALLY
cages = []

class Animal:
   def __init__(self, name):
        self.name = name

class Cage:
    def __init__(self, no):
        self.no = no
        self.animals = []

def menu():
    print("\n***** WELCOME TO VIRTUAL ZOO *****")
    print("[1] Add Animal")
    print("[2] Create Cage")
    print("[3] Show Animals")
    print("[4] Transfer Animals")
    print("Input: ", end = '')
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
        transfer_animal()
    else:
        print("Input no. is not in the menu. Please try again.")
        menu()

def addAnimal():
    x = len(cages)
    if x == 0:
        print("No cages yet.")
        menu()
    else:
        print("Enter cage no.: ", end = '')
        x = input()
        x = int(x)
        for cage in cages:
            if cage.no == x:
                print("Enter animals name: ", end = '')
                animal_name = input()
                newanimal = Animal(animal_name)
                animals.append(newanimal)
                cage.animals.append(newanimal)
                print("Animal successfully added.")
        menu()

def create_cage():
    print("Enter cage no.: ", end = '')
    x = input()
    x = int(x)
    for cage in cages:
        if cage.no == x:
            print("Cage no. already exist.")
            menu()
    cages.append(Cage(x))
    print("Cage successfully created.")
    menu()

def show_animal():
    for x in cages:
        print('-Cage no. ', x.no)
        for y in x.animals:
            print('--',y.name)
    menu()
    
def transfer_animal():
    print("Enter source cage no.: ", end = '')
    x = input()
    x = int(x)
    print("Enter destination cage no.: ", end = '')
    y = input()
    y = int(y)
    print("Enter animal name: ", end = '')
    z = input()
    for animal in animals:
        if animal.name == z:
            for cage in cages:
                if cage.no == x:
                    cage.animals.remove(animal)
                if cage.no == y:
                    cage.animals.append(animal)
    menu()
menu()
