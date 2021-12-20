import csv
from os import read
import time

with open("./data/PP_recipes2.csv", mode="w",
          encoding="utf-8") as employee_file:

    with open("./data/PP_recipes.csv", "r", encoding="utf-8") as file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=",",
                                     quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['item_id', 'ingredients'])
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            temp = [
                row[1],
                "|".join(row[7].replace("[", "").replace("]", "").split(", "))
            ]
            employee_writer.writerow(temp)

            # print(row[2], id, url)

            # print(row)
