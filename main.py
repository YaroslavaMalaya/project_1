import sys

file1 = sys.argv[1]

with open("olympics.tsv", "r") as file:
    line = file.readline()
    while line != "":
        line = file.readline()
        split = line.split("\t")
        print(split)

# country = sys.argv[3]
# values = [x for x in sys.argv[2:]]
# print(values)

if len(sys.argv) > 6:
    print("error")
    exit()
