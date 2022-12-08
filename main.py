import sys

print(len(sys.argv[1:]))

country = sys.argv[3]

if len(sys.argv) > 6:
    print("error")
    exit()


# with open("Olympic Athletes - athlete_events.tsv") as file:
#     headline = file.readline().split("/t")
