import argparse


def find_medals(country, game, filename):
    names = []
    medals = []
    counter = 0
    for_new = ["First ten medalists."]
    with open(filename, "r") as file:
        file.readline()  # headline
        line = file.readline()
        print("First ten medalists.")
        while line != "":
            new_line = line.split("\t")
            if country == new_line[7] and game in new_line[8]:
                while counter < 10:
                    if new_line[1] not in names and new_line[-1] != "NA\n":
                        m = new_line[-1].split("\n")[0]
                        print(f"{counter + 1}) {new_line[1]} - {new_line[12]} - {m}")
                        for_new.append(f"{counter + 1}) {new_line[1]} - {new_line[12]} - {m}")
                        counter += 1
                        names.append(new_line[1])
                    else:
                        break
                medals.append(new_line[-1])
            line = file.readline()
    check(new_line, counter)
    return medals, for_new


def check(names, counter):
    if len(names) == 0:
        print("This country and/or year didn't take part in games.")
        quit()
    elif counter < 10:
        print("This country has less than 10 medals((((")
        quit()


def get_output_medals(newfile, for_new):
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
                    country_medals[new_line[6]] = [new_line[-1].split("\n")[0]]
                else:
                    country_medals[new_line[6]].append(new_line[-1].split("\n")[0])
            line = file.readline()

    if len(country_medals) == 0:
        print("Invalid year. This year didn't take part in games.")
    else:
        for country_t in country_medals:
            for medal_t in country_medals.get(country_t):
                print(f"{country_t}: {medal_t}")


def overall(country, filename):
    medals_year = {

    }
    with open(filename, "r") as file:
        file.readline()  # headline
        line = file.readline()
        while line != "":
            new_line = line.split("\t")
            if country == new_line[6] or country == new_line[7]:
                if new_line[-1] != "NA\n" and new_line[9] not in medals_year:
                    medals_year[new_line[9]] = 1
                elif new_line[-1] != "NA\n":
                    medals_year[new_line[9]] += 1
            line = file.readline()

    return medals_year.items()


def count_medals(medals, for_new):   # for_new
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
    for_new.append(f"amount of gold medals {gold}\namount of silver medals {silver}\namount of bronze medals {bronze}")
    return gold + silver + bronze


def check_first(country, filename):
    min_year = 1000000
    with open(filename, "r") as file:
        file.readline()  # headline
        line = file.readline()
        while line != "":
            new_line = line.split("\t")
            if country == new_line[6] or country == new_line[7]:
                year = int(new_line[9])
                if year < min_year:
                    min_year = year
                    city = new_line[11]
            line = file.readline()
        return min_year, city


def interactive(country, filename):
    with open(filename, "r") as file:
        file.readline()  # headline
        line = file.readline()
        while line != "":
            new_line = line.split("\t")
            if country == new_line[6] or country == new_line[7]:
                min_year1, city = check_first(country, filename)
                yearx, maximum = max(overall(country, filename))
                yearm, minimum = min(overall(country, filename))
                print(f"First attendance in {min_year1} in {city}.")
                print(f"The most successful olympiad in {yearx} had {maximum} medals.")
                print(f"The most successful olympiad in {yearm} had {minimum} medals.")
                exit()
            line = file.readline()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('--medals', '-m',  help="Enter country and a year to count medals", type=str, nargs='+')
    parser.add_argument('--output')
    parser.add_argument('--total', '-t', help="Enter year to find number of medals", type=str, nargs='+')
    parser.add_argument('--overall', '-o', help="Enter list of countries", nargs='+')
    parser.add_argument('--interactive', '-i', help="Enter the country", type=str)
    args = parser.parse_args()
    filename = args.filename
    print(args)
    if args.medals and not args.output:
        country = args.medals[0]
        year = args.medals[1]
        game = args.medals[2]
        game_and_year = year + " " + game
        medals, for_new = find_medals(country, game_and_year, filename)
        print(f"In general {count_medals(medals, for_new)} medals.")
    if args.output and args.medals:
        country = args.medals[0]
        year = args.medals[1]
        game = args.medals[2]
        game_and_year = year + " " + game
        medals, for_new = find_medals(country, game_and_year, filename)
        print(f"In general {count_medals(medals, for_new)} medals.")
        newfile = args.output
        get_output_medals(newfile, for_new)
    if args.total:
        year = args.total[0]
        print(year)
        print(total(year, filename))
    if args.overall:
        for country in args.overall:
            byear, mmmedals = max(overall(country, filename))
            print(f"For {country} in {byear} the biggest amount of medals is {mmmedals}")
    if args.interactive:
        country = input("Enter the country for statistics: ")
        print(interactive(country, filename))


if __name__ == "__main__":
    main()
