import csv
from os import read
import time

with open("./data/interactions_train2.csv", mode="w",
          encoding="utf-8") as employee_file:

    with open("./data/interactions_train.csv", "r", encoding="utf-8") as file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=",",
                                     quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(
            ['date', 'TIMESTAMP', 'rating', 'USER_ID', 'ITEM_ID'])
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if (float(row[2]) >= 4):
                employee_writer.writerow(row)

            # print(row[2], id, url)

            # print(row)
