import sys

file1 = sys.argv[1]
country = input("Enter a country: ")

with open("olympics.tsv", "r") as file:
    line = file.readline()
    while line != "":
        split = line.split("\t")
        if country == split[7]:
            print(split)
        line = file.readline()






# country = sys.argv[3]
# values = [x for x in sys.argv[2:]]
# print(values)
