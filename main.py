import sys

file1 = sys.argv[0]


def medals(country, game):
    names = []
    medals = []
    counter = 0
    with open("olympics.tsv", "r") as file:
        file.readline()                         # headline
        line = file.readline()
        while line != "":
            new_line = line.split("\t")
            if country == new_line[7] and game in new_line[8]:
                while counter < 10:
                    if new_line[1] not in names and new_line[-1] != "NA\n":
                        m = new_line[-1].split("\n")[0]
                        print("First ten medalists.")
                        print(f"{counter+1}) {new_line[1]} - {new_line[12]} - {m}")
                        counter += 1
                        names.append(new_line[1])
                    else:
                        break
                medals.append(new_line[-1])
            line = file.readline()


def total():
    pass


country = input("Enter a country: ")
game = input("Enter a game: ")
mode = input("Enter a command: ")

if mode == "-total":
    total()
elif mode == "-medal":
    medals(country, game)

