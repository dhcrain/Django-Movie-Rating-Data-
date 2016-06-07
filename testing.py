import csv


with open("data/u.item", encoding='latin1') as infile:
    rating = csv.reader(infile, delimiter="|")
    for row in rating:
        print(row[4])