import csv
from random import random

file = open('books.csv', 'r')
total_count = 0
short_title_count = 0
table = list(csv.reader(file, delimiter = ';'))

for index, row in enumerate(table):
    if index == 0:
        continue

    title = row[1]

    if len(title) > 30:
        short_title_count += 1

    total_count += 1

print("Кол-во книг: ", total_count)
print("Кол-во книг < 30 символов: ", short_title_count)

search_author = input('Введите автора: ').lower()

for index, row in enumerate(table):
    if index == 0:
        continue

    date = row[6]
    year = int(date[6:10])

    if year < 2018:
        continue

    author = row[3]

    if author.lower() == search_author:
        print(row[3], "-", row[1], "-", row[6])

output = open("output.txt", "w")
output_count = 0
for index, row in enumerate(table):
    if index == 0:
        continue

    if random() < 0.2 and output_count < 20:
        output_count += 1
        print(f"#{index} {row[4]}. {row[1]} - {row[6]}", file = output)

output.close()
file.close()


