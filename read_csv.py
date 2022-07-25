import csv

path = "data/addresses.csv"

with open(path, newline='') as csvfile:

   reader = csv.reader(csvfile)

   for row in reader:

      for col in row:

         print(col,end=" ")

      print()