import argparse


def find_medals(filename, country, year):
    names = []
    medals = []
    counter = 0
    for_new = ["First ten medalists."]
    print("First ten medalists.")
    with open(filename, "r") as file:
        file.readline()  # headline
        line = file.readline()
        while line != "":
            new_line = line.split("\t")
            if country in new_line[7] and year in new_line[9]:
                if counter < 10 and new_line[-1] != "NA\n":
                    m = new_line[-1].split("\n")[0]
                    print(f'{counter + 1}) {new_line[1]} - {new_line[12]} - {m}')
                    for_new.append(str(f'{counter + 1}) {new_line[1]} - {new_line[12]} - {m}'))
                    counter += 1
                    names.append(new_line[1])
                medals.append(new_line[-1])
            line = file.readline()
    count_medals(medals, for_new)
    check(names, counter)
    return for_new


def check(names, counter):
    if len(names) == 0:
        print("This country and/or year didn't take part in games.")
        quit()
    elif counter < 10:
        print("This country has less than 10 medals((((")
        quit()


def get_output_medals(filename, country, year, newfile):
    for_new = find_medals(filename, country, year)
    with open(newfile, "w+") as n_file:
        for line in for_new:
            print(line, file=n_file)


def total(year, filename):
    country_medals = {

    }
    print(f"Countries with medals in {year}.")
    with open(filename, "r") as file:
        file.readline()  # headline
        line = file.readline()
        while line != "":
            new_line = line.split("\t")
            if year == new_line[9] and new_line[-1] != 'NA\n':
                if new_line[6] not in country_medals:
                    country_medals[new_line[6]] = [new_line[-1]]
                else:
                    country_medals[new_line[6]].append(new_line[-1])
            line = file.readline()

    if len(country_medals) == 0:
        print("Invalid year. This year didn't take part in games.")
    else:
        for country_t in country_medals:
            for medal_t in country_medals.get(country_t):
                print(f"{country_t}: {medal_t}")


def count_medals(medals, for_new):
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
    # for_new.append(f"amount of gold medals {gold}\namount of silver medals {silver}\namount of bronze medals {bronze} ")
    return gold + silver + bronze

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('--medals', '-m',  help="Enter country and a year to count medals", type=str, nargs='+')
    parser.add_argument('--output')
    parser.add_argument('--total', '-t', help="Enter year to find number of medals", type=str, nargs='+')
    parser.add_argument('--overall', '-o', help="Enter list of countries", nargs='+')
    args = parser.parse_args()
    print(args)
    if args.medals:
        country = args.medals[0]
        year = args.medals[1]
        game = args.medals[2]
        game_and_year = year + " " + game
        medals = find_medals(country, game_and_year)
        count_medals(medals)
    if args.total:
        year = args.total[0]
        print(year)
        print(total(year, "olympics.tsv"))
    if args.overall:
        for country in args.overall:
            pass
            # print(overall(country))

if __name__ == "__main__":
    main()
