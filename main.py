import sys

file1 = sys.argv[0]


def check(new_line, counter):
    if country in new_line[7]:
        find_medals(country, game)
    elif country not in new_line[7]:
        print("This country didn't take part in games.")
        exit()
    elif game not in new_line[8]:
        print("Invalid year.")
        exit()
    elif counter < 10:
        print("This country has less than 10 medals((((")
        exit()



def find_medals(country, game):
    names = []
    medals = []
    counter = 0
    with open("olympics.tsv", "r") as file:
        file.readline()                         # headline
        line = file.readline()
        print("First ten medalists.")
        while line != "":
            new_line = line.split("\t")
            if country == new_line[7] and game in new_line[8]:
                while counter < 10:
                    if new_line[1] not in names and new_line[-1] != "NA\n":
                        m = new_line[-1].split("\n")[0]
                        print(f"{counter+1}) {new_line[1]} - {new_line[12]} - {m}")
                        counter += 1
                        names.append(new_line[1])
                    else:
                        break
                medals.append(new_line[-1])
            line = file.readline()
    # check(new_line, counter)
    return medals


def add_in_file():
    pass

def count_medals():
    medals = find_medals(country, game)
    gold = 0
    silver = 0
    bronze = 0
    for medal in medals:
        if "Gold\n" in medal:
            gold += 1
        if "Silver\n" in medal:
            silver += 1
        if "Bronze\n" in medal:
            bronze += 1
    print(f"amount of gold medals {gold}\namount of silver medals {silver}\namount of bronze medals {bronze} ")

def total():
    pass


country = input("Enter a country: ")
game = input("Enter a game: ")
mode = input("Enter a command: ")

if mode == "-total":
    total()
elif mode == "-medal":
    count_medals()
elif mode == "-output":
    find_medals(country, game)

