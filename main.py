import argparse

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

def total(year):
    countries = []
    country_medals = {}
    medals = []
    counter = 0
    with open("olympics.tsv", "r") as file:
        file.readline()  # headline
        line = file.readline()
        while line != "":
            new_line = line.split("\t")
            if year == new_line[9] and new_line[14] != 'NA\n':
                country_medals[new_line[6]] = new_line[-1]

    # check(new_line, counter)
    return country_medals


def count_medals(medals, country, game):
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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-medals',  help="Enter country and a year to count medals", type=str, nargs='+')
    parser.add_argument('-total', help="Enter year to find number of medals", type=str, nargs='+')
    args = parser.parse_args()
    print(args)
    if args.medals:
        country = args.medals[0]
        year = args.medals[1]
        game = args.medals[2]
        medals = find_medals(country, year)
        count_medals(medals, country, game)
    if args.total:
        year = args.total[0]
        print(year)
        print(total(year))

if __name__ == "__main__":
    main()

# def check(new_line, counter):
#     if country in new_line[7]:
#         find_medals(country, game)
#     elif country not in new_line[7]:
#         print("This country didn't take part in games.")
#         exit()
#     elif game not in new_line[8]:
#         print("Invalid year.")
#         exit()
#     elif counter < 10:
#         print("This country has less than 10 medals((((")
#         exit()


def add_in_file():
    pass




