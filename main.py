import sys
file = sys.argv[1]
with open("olympics.tsv") as file:
    headline = file.readline().split("/t")
# print(len(sys.argv[1:]))

country = sys.argv[3]
values = [x for x in sys.argv[2:]]
print(values)

if len(sys.argv) > 6:
    print("error")
    exit()


